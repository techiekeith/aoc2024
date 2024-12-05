import unittest

from ..day3 import Day3, find_enabled_statements, find_mul_statements, multiply_numbers

class TestDay3(unittest.TestCase):
    day3 = Day3()

    def test_init(self):
        self.day3.load("inputs/day3/test_input_part_1.txt")
        expected = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        actual = self.day3.program.strip()
        self.assertEqual(expected, actual)

    def test_find_mul_statements_part_1(self):
        self.day3.load("inputs/day3/test_input_part_1.txt")
        expected = [(2, 4), (5, 5), (11, 8), (8, 5)]
        actual = find_mul_statements(self.day3.program)
        self.assertEqual(expected, actual)

    def test_multiply_numbers_part_1(self):
        self.day3.load("inputs/day3/test_input_part_1.txt")
        expected = 161
        actual = multiply_numbers(self.day3.program)
        self.assertEqual(expected, actual)

    def test_find_mul_statements_part_2(self):
        self.day3.load("inputs/day3/test_input_part_2.txt")
        expected = [(2, 4), (8, 5)]
        actual = find_mul_statements(find_enabled_statements(self.day3.program))
        self.assertEqual(expected, actual)

    def test_multiply_numbers_part_2(self):
        self.day3.load("inputs/day3/test_input_part_2.txt")
        expected = 48
        actual = multiply_numbers(find_enabled_statements(self.day3.program))
        self.assertEqual(expected, actual)
