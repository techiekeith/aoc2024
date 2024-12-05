import unittest
from ..day2 import Day2, is_report_safe, is_report_mostly_safe


class TestDay2(unittest.TestCase):
    day2 = Day2()
    day2.load("inputs/day2/test_input.txt")

    def test_init(self):
        expected = [
            [7,6,4,2,1],
            [1,2,7,8,9],
            [9,7,6,2,1],
            [1,3,2,4,5],
            [8,6,4,4,1],
            [1,3,6,7,9],
        ]
        actual = self.day2.reports
        self.assertEqual(expected, actual)

    def test_safe_descending_sequence(self):
        sequence = [7,6,4,2,1]
        result = is_report_safe(sequence)
        self.assertEqual(result, True)

    def test_unsafe_ascending_sequence(self):
        sequence = [1,2,7,8,9]
        result = is_report_safe(sequence)
        self.assertEqual(result, False)

    def test_very_unsafe_ascending_sequence(self):
        sequence = [1,2,7,8,9]
        result = is_report_mostly_safe(sequence)
        self.assertEqual(result, False)

    def test_unsafe_descending_sequence(self):
        sequence = [9,7,6,2,1]
        result = is_report_safe(sequence)
        self.assertEqual(result, False)

    def test_very_unsafe_descending_sequence(self):
        sequence = [9,7,6,2,1]
        result = is_report_mostly_safe(sequence)
        self.assertEqual(result, False)

    def test_unsafe_mixed_sequence(self):
        sequence = [1,3,2,4,5]
        result = is_report_safe(sequence)
        self.assertEqual(result, False)

    def test_mostly_safe_mixed_sequence(self):
        sequence = [1,3,2,4,5]
        result = is_report_mostly_safe(sequence)
        self.assertEqual(result, True)

    def test_unsafe_descending_sequence_with_duplicate(self):
        sequence = [8,6,4,4,1]
        result = is_report_safe(sequence)
        self.assertEqual(result, False)

    def test_mostly_safe_descending_sequence_with_duplicate(self):
        sequence = [8,6,4,4,1]
        result = is_report_mostly_safe(sequence)
        self.assertEqual(result, True)

    def test_safe_ascending_sequence(self):
        sequence = [1,3,6,7,9]
        result = is_report_safe(sequence)
        self.assertEqual(result, True)

    def test_count_safe_reports(self):
        expected = 2
        actual = self.day2.count_safe_reports()
        self.assertEqual(expected, actual)

    def test_count_mostly_safe_reports(self):
        expected = 4
        actual = self.day2.count_mostly_safe_reports()
        self.assertEqual(expected, actual)
