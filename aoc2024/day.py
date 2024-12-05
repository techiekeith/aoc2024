from abc import abstractmethod


class Day:
    @abstractmethod
    def load(self, input_file):
        pass

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass
