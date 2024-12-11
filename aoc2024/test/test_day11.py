import unittest
from ..day11 import Day11, blink



class TestDay11(unittest.TestCase):
    def setUp(self):
        self.day11 = Day11()
        self.day11.load("inputs/day11/test_input.txt")

    def test_load(self):
        expected = {125: 1, 17: 1}
        actual = self.day11.stones
        self.assertEqual(expected, actual)

    def test_blink_first_example(self):
        stones = {0: 1, 1: 1, 10: 1, 99: 1, 999: 1}
        expected = 7
        actual = blink(stones)
        self.assertEqual(expected, actual)

    def test_blink_once(self):
        stones = {125: 1, 17: 1}
        expected = 3
        actual = blink(stones)
        self.assertEqual(expected, actual)

    def test_blink_six_times(self):
        stones = {125: 1, 17: 1}
        expected = 22
        actual = blink(stones, 6)
        self.assertEqual(expected, actual)
