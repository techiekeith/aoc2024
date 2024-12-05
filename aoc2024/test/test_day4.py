import unittest
from ..day4 import Day4

class TestDay4(unittest.TestCase):
    day4 = Day4()
    day4.load("inputs/day4/test_input.txt")

    def test_init(self):
        expected_first_row = ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"]
        expected_last_row = ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"]
        actual = self.day4.rows
        self.assertEqual(expected_first_row, actual[0])
        self.assertEqual(expected_last_row, actual[-1])

    def test_find_starting_positions(self):
        expected_first_result = (0, 4)
        expected_last_result = (9, 9)
        actual = self.day4.find_starting_positions("XMAS")
        self.assertEqual(expected_first_result, actual[0])
        self.assertEqual(expected_last_result, actual[-1])

    def test_position_is_in_bounds(self):
        self.assertTrue(self.day4.position_is_in_bounds((0, 0)))
        self.assertTrue(self.day4.position_is_in_bounds((0, 9)))
        self.assertTrue(self.day4.position_is_in_bounds((9, 0)))
        self.assertTrue(self.day4.position_is_in_bounds((9, 9)))
        self.assertFalse((self.day4.position_is_in_bounds((-1, 0))))
        self.assertFalse((self.day4.position_is_in_bounds((0, -1))))
        self.assertFalse((self.day4.position_is_in_bounds((10, 0))))
        self.assertFalse((self.day4.position_is_in_bounds((0, 10))))

    def test_word_matches_position_and_direction(self):
        self.assertTrue(self.day4.word_matches_position_and_direction("XMAS", (0, 4), (1, 1)))
        self.assertTrue(self.day4.word_matches_position_and_direction("XMAS", (0, 5), (0, 1)))
        self.assertTrue(self.day4.word_matches_position_and_direction("XMAS", (5, 6), (-1, -1)))

    def test_word_search_from_starting_position(self):
        self.assertEqual(1, self.day4.word_search_from_starting_position("XMAS", (0, 4)), )
        self.assertEqual(2, self.day4.word_search_from_starting_position("XMAS", (9, 9)), )
        self.assertEqual(0, self.day4.word_search_from_starting_position("XMAS", (0, 0)), )

    def test_count_all_word_matches(self):
        self.assertEqual(18, self.day4.count_all_word_matches("XMAS"))

    def test_count_all_cross_matches(self):
        self.assertEqual(9, self.day4.count_all_cross_matches("MAS"))
