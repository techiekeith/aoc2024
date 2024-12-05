import unittest
from ..day1 import Day1

class TestDay1(unittest.TestCase):
    day1 = Day1()

    def test_left_numbers(self):
        self.day1.load("inputs/day1/test_input.txt")
        actual = self.day1.left_numbers
        expected = [3,4,2,1,3,3]
        self.assertEqual(expected, actual)

    def test_right_numbers(self):
        self.day1.load("inputs/day1/test_input.txt")
        actual = self.day1.right_numbers
        expected = [4,3,5,3,9,3]
        self.assertEqual(expected, actual)

    def test_sum_of_sorted_distances(self):
        self.day1.load("inputs/day1/test_input.txt")
        actual = self.day1.sum_of_sorted_distances()
        expected = 11
        self.assertEqual(expected, actual)

    def test_similarity_score(self):
        self.day1.load("inputs/day1/test_input.txt")
        actual = self.day1.similarity_score()
        expected = 31
        self.assertEqual(expected, actual)
