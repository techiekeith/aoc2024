import unittest
from ..day8 import Day8, find_antinodes


class TestDay8(unittest.TestCase):
    def setUp(self):
        self.day8 = Day8()
        self.day8.load("inputs/day8/test_input.txt")

    def test_load(self):
        expected_first_group = [(8, 1), (5, 2), (7, 3), (4, 4)]
        expected_second_group = [(6, 5), (8, 8), (9, 9)]
        self.assertEqual(self.day8.antennae["0"], expected_first_group)
        self.assertEqual(self.day8.antennae["A"], expected_second_group)
        self.assertFalse("." in self.day8.antennae)

    def test_find_antinodes(self):
        coordinates = [(6, 5), (8, 8), (9, 9)]
        expected = {(0, 0): 1, (3, 1): 1, (4, 2): 1, (7, 7): 1, (10, 10): 1, (10, 11): 1}
        self.assertEqual(expected, find_antinodes(12, 12, coordinates, {(0, 0): 1}))

    def test_count_antinodes(self):
        self.assertEqual(14, self.day8.count_antinodes())

    def test_count_antinodes_with_repeat(self):
        self.assertEqual(34, self.day8.count_antinodes(repeat=True))
