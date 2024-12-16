import unittest

from ..day16 import Day16, Location


class TestDay16(unittest.TestCase):
    def setUp(self):
        self.day16 = Day16()

    def test_load(self):
        self.day16.load("inputs/day16/test_input_1.txt")
        expected_row = [char for char in "#.......#....E#"]
        self.assertEqual(expected_row, self.day16.grid[1])

    def test_find_start_1(self):
        self.day16.load("inputs/day16/test_input_1.txt")
        expected = (1, 13)
        self.day16.find_start()
        self.assertEqual(expected, self.day16.start)

    def test_find_end_1(self):
        self.day16.load("inputs/day16/test_input_1.txt")
        expected = (13, 1)
        self.day16.find_end()
        self.assertEqual(expected, self.day16.end)

    def test_find_next_paths_1(self):
        self.day16.load("inputs/day16/test_input_1.txt")
        self.day16.reset()
        expected_paths = [
            Location((2, 13), (1, 0), 1),
            Location((1, 13), (0, -1), 1000, rotated=True)
        ]
        expected_visited = { ((1, 13), (1, 0)): Location(self.day16.start, start=True) }
        actual_paths, actual_visited = self.day16.find_next_paths()
        self.assertEqual(expected_paths, actual_paths)
        self.assertEqual(expected_visited, actual_visited)

    def test_find_best_score_1(self):
        self.day16.load("inputs/day16/test_input_1.txt")
        self.day16.reset()
        expected = 7036
        actual, visited = self.day16.run()
        self.assertEqual(expected, actual)

    def test_find_best_score_2(self):
        self.day16.load("inputs/day16/test_input_2.txt")
        self.day16.reset()
        expected = 11048
        actual, visited = self.day16.run()
        self.assertEqual(expected, actual)
