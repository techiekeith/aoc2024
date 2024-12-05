import re

from aoc2024.day import Day


def find_mul_statements(program):
    return [(int(a), int(b)) for a, b in re.findall(r"mul\((\d+),(\d+)\)", program)]


def multiply_numbers(program):
    return sum([a * b for a, b in find_mul_statements(program)])


def find_enabled_statements(program):
    return "".join([re.split(r"don't\(\)", x)[0] for x in re.split(r"do\(\)", program)])


class Day3(Day):
    def __init__(self):
        self.program = None

    def load(self, input_file):
        self.program = None
        with open(input_file) as file:
            self.program = file.read()

    def part1(self):
        return multiply_numbers(self.program)

    def part2(self):
        return multiply_numbers(find_enabled_statements(self.program))
