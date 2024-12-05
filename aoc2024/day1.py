from aoc2024.day import Day


class Day1(Day):
    def __init__(self):
        self.left_numbers = None
        self.right_numbers = None
        self.right_dict = None

    def load(self, input_file):
        self.left_numbers = []
        self.right_numbers = []
        self.right_dict = {}
        with open(input_file, 'r') as file:
            while line := file.readline():
                [lhs, rhs] = line.split()
                # Plain old arrays for part 1
                self.left_numbers.append(int(lhs))
                self.right_numbers.append(int(rhs))
                # Dictionary for part 2
                if int(rhs) not in self.right_dict:
                    self.right_dict[int(rhs)] = 0
                self.right_dict[int(rhs)] = self.right_dict[int(rhs)] + 1

    def sum_of_sorted_distances(self):
        lhs_sorted = sorted(self.left_numbers)
        rhs_sorted = sorted(self.right_numbers)
        distance_sum = 0

        for i in range(0, len(lhs_sorted)):
            distance_sum += abs(lhs_sorted[i] - rhs_sorted[i])

        return distance_sum

    def similarity_score(self):
        score = 0
        for lhs in self.left_numbers:
            if lhs in self.right_dict:
                score = score + lhs * self.right_dict[lhs]
        return score

    def part1(self):
        return self.sum_of_sorted_distances()

    def part2(self):
        return self.similarity_score()
