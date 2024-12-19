from aoc2024.day import Day


def count_matches(design, patterns, memo):
    if design == "":
        return 1
    result = 0
    if design in memo:
        return memo[design]
    for pattern in patterns:
        if design.startswith(pattern):
            result += count_matches(design[len(pattern):], patterns, memo)
    memo[design] = result
    return result


def memoize_patterns(patterns):
    memo = {}
    for index in range(len(patterns)):
        memo[patterns[index]] = count_matches(patterns[index], patterns, memo)
    return memo


def count_possible_designs(designs, patterns, memo):
    return sum(1 if count_matches(design, patterns, memo) > 0 else 0 for design in designs)


def count_design_permutations(designs, patterns, memo):
    return sum(count_matches(design, patterns, memo) for design in designs)


class Day19(Day):
    patterns = None
    designs = None
    matching_designs = None
    memo = None

    def load(self, input_file):
        self.patterns = None
        self.designs = []
        self.matching_designs = None
        with open(input_file) as f:
            while line := f.readline():
                if self.patterns is None:
                    self.patterns = [pattern.strip() for pattern in line.split(',')]
                else:
                    design = line.strip()
                    if design != "":
                        self.designs.append(design)
        self.memo = memoize_patterns(self.patterns)

    def part1(self):
        return count_possible_designs(self.designs, self.patterns, self.memo)

    def part2(self):
        return count_design_permutations(self.designs, self.patterns, self.memo)

    def is_performance_slow(self):
        return True
