import math

from aoc2024.day import Day


def equation_may_be_true(equation, allow_concatenation=False):
    (test_value, operand_list) = equation
    if len(operand_list) == 1:
        return test_value == operand_list[0]
    lhs = operand_list[0]
    rhs = operand_list[1]
    remaining_operands = operand_list[2:]
    add = lhs + rhs
    if add <= test_value and equation_may_be_true((test_value, [add] + remaining_operands), allow_concatenation):
        return True
    multiply = lhs * rhs
    if multiply <= test_value and equation_may_be_true((test_value, [multiply] + remaining_operands), allow_concatenation):
        return True
    if allow_concatenation:
        concat = lhs * 10 ** (1 + math.floor(math.log10(rhs))) + rhs
        if concat <= test_value and equation_may_be_true((test_value, [concat] + remaining_operands), allow_concatenation):
            return True
    return False

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
                    if equation_may_be_true((test_value, operand_list), allow_concatenation)])

    def part1(self):
        return self.get_total_calibration_result()

    def part2(self):
        return self.get_total_calibration_result(allow_concatenation=True)

    def is_part2_performance_slow(self):
        return True
