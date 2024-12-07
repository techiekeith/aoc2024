import math

from aoc2024.day import Day


def find_operators(equation, allow_concatenation = False):
    (test_value, operand_list) = equation
    if len(operand_list) == 1:
        if test_value == operand_list[0]:
            return [[]]
        return []
    operators = []
    multiply = operand_list[0] * operand_list[1]
    add = operand_list[0] + operand_list[1]
    if multiply <= test_value:
        operators += [["*"] + others for others in find_operators((test_value, [multiply] + operand_list[2:]), allow_concatenation)]
    if add <= test_value:
        operators += [["+"] + others for others in find_operators((test_value, [add] + operand_list[2:]), allow_concatenation)]
    if allow_concatenation:
        concat = int(f"{operand_list[0]}{operand_list[1]}")
        if concat <= test_value:
            operators += [["||"] + others for others in find_operators((test_value, [concat] + operand_list[2:]), allow_concatenation)]
    return operators


class Day7(Day):
    equations = None

    def load(self, input_file):
        self.equations = []
        with open(input_file, 'r') as file:
            while line := file.readline():
                [test_value_str, operands] = line.strip().split(":")
                test_value = int(test_value_str)
                operand_list = [int(operand) for operand in operands.split()]
                self.equations.append((test_value, operand_list))

    def get_total_calibration_result(self, allow_concatenation = False):
        return sum([test_value for test_value, operand_list in self.equations
                    if len(find_operators((test_value, operand_list), allow_concatenation)) > 0])

    def part1(self):
        return self.get_total_calibration_result()

    def part2(self):
        return self.get_total_calibration_result(allow_concatenation=True)
