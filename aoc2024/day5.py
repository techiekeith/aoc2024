from aoc2024.day import Day


def order_matches_rule(page_ordering_rules, rule):
    return page_ordering_rules.get(rule) is not None


def update_is_ordered(page_ordering_rules, update):
    for index in range(len(update) - 1):
        a = update[index]
        for nextIndex in range(index + 1, len(update)):
            b = update[nextIndex]
            if order_matches_rule(page_ordering_rules, (b, a)):
                return False
            if order_matches_rule(page_ordering_rules, (a, b)):
                continue
            print(f"No rule matching {a} -> {b}")
    return True


def get_ordered_updates(page_ordering_rules, updates):
    return [update for update in updates if update_is_ordered(page_ordering_rules, update)]


def get_middle_value(update):
    return update[int(len(update) / 2)]


def get_disordered_updates(page_ordering_rules, updates):
    return [update for update in updates if not update_is_ordered(page_ordering_rules, update)]


def correct_update_order(page_ordering_rules, update):
    corrected_update = [x for x in update]
    for index in range(len(corrected_update) - 1):
        a = corrected_update[index]
        next_index = index + 1
        while next_index < len(corrected_update):
            b = corrected_update[next_index]
            if order_matches_rule(page_ordering_rules, (b, a)):
                corrected_update = corrected_update[:index] + [b, a] + corrected_update[index + 1:next_index] + corrected_update[next_index + 1:]
                a = b
                next_index = index + 1
            next_index += 1
    return corrected_update

class Day5(Day):
    def __init__(self):
        self.page_ordering_rules = None
        self.updates = None

    def load(self, input_file):
        self.page_ordering_rules = {}
        self.updates = []
        with open(input_file, 'r') as file:
            line_number = 0
            while line := file.readline():
                line = line.strip()
                line_number += 1
                if line.find("|") > 0:
                    [a, b] = [int(x) for x in line.split("|")]
                    self.page_ordering_rules[(a, b)] = line_number
                    continue
                if line.find(",") > 0:
                    self.updates.append([int(x) for x in line.split(",")])

    def get_total_middle_values_of_ordered_updates(self):
        return sum([get_middle_value(update) for update in get_ordered_updates(self.page_ordering_rules, self.updates)])

    def get_total_middle_values_of_disordered_updates(self):
        return sum([get_middle_value(correct_update_order(self.page_ordering_rules, update))
                    for update in get_disordered_updates(self.page_ordering_rules, self.updates)])

    def part1(self):
        return self.get_total_middle_values_of_ordered_updates()

    def part2(self):
        return self.get_total_middle_values_of_disordered_updates()
