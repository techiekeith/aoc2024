import unittest
from ..day7 import Day7, equation_may_be_true


class TestDay7(unittest.TestCase):
    def setUp(self):
        self.day7 = Day7()
        self.day7.load("inputs/day7/test_input.txt")

    def test_load(self):
        expected_first_equation = (190, [10, 19])
        expected_last_equation = (292, [11, 6, 16, 20])
        self.assertEqual(9, len(self.day7.equations))
        self.assertEqual(expected_first_equation, self.day7.equations[0])
        self.assertEqual(expected_last_equation, self.day7.equations[8])

    def test_find_operators_first(self):
        equation = (190, [10, 19])
        self.assertTrue(equation_may_be_true(equation))

    def test_find_operators_second(self):
        equation = (3267, [81, 40, 27])
        self.assertTrue(equation_may_be_true(equation))

    def test_find_operators_last(self):
        equation = (292, [11, 6, 16, 20])
        self.assertTrue(equation_may_be_true(equation))

    def test_get_total_calibration_result(self):
        self.assertEqual(3749, self.day7.get_total_calibration_result())

    def test_find_operators_fourth_with_concatenation(self):
        equation = (156, [15, 6])
        self.assertFalse(equation_may_be_true(equation))
        self.assertTrue(equation_may_be_true(equation, allow_concatenation=True))

    def test_find_operators_fifth_with_concatenation(self):
        equation = (7290, [6, 8, 6, 15])
        self.assertFalse(equation_may_be_true(equation))
        self.assertTrue(equation_may_be_true(equation, allow_concatenation=True))

    def test_find_operators_seventh_with_concatenation(self):
        equation = (192, [17, 8, 14])
        self.assertFalse(equation_may_be_true(equation))
        self.assertTrue(equation_may_be_true(equation, allow_concatenation=True))

    def test_get_total_calibration_result_with_concatenation(self):
        self.assertEqual(11387, self.day7.get_total_calibration_result(allow_concatenation=True))
