import unittest

from ..day18 import Day18


class TestDay18(unittest.TestCase):
    def setUp(self):
        self.day18 = Day18(size=6)

    def test_load(self):
        self.day18.load("inputs/day18/test_input.txt")
        self.assertEqual(25, len(self.day18.corrupted_bytes))
        self.assertEqual((5, 4), self.day18.corrupted_bytes[0])
        self.assertEqual((2, 0), self.day18.corrupted_bytes[24])

    def test_get_corrupted_bytes_dict(self):
        self.day18.load("inputs/day18/test_input.txt")
        expected = {
            (5, 4): 1,
            (4, 2): 1,
            (4, 5): 1,
            (3, 0): 1,
            (2, 1): 1,
            (6, 3): 1,
            (2, 4): 1,
            (1, 5): 1,
            (0, 6): 1,
            (3, 3): 1,
            (2, 6): 1,
            (5, 1): 1,
        }
        actual = self.day18.get_corrupted_bytes_dict(size=12)
        self.assertEqual(expected, actual)

    def test_find_next_paths(self):
        self.day18.load("inputs/day18/test_input.txt")
        corrupted_bytes_dict = self.day18.get_corrupted_bytes_dict(size=12)
        expected_paths = [ (0, 1), (1, 0) ]
        expected_visited_dict = { (0, 0): 1 }
        actual_paths, actual_visited_dict = self.day18.find_next_paths(corrupted_bytes_dict)
        self.assertEqual(expected_paths, actual_paths)
        self.assertEqual(expected_visited_dict, actual_visited_dict)

    def test_run(self):
        self.day18.load("inputs/day18/test_input.txt")
        expected = 22
        actual = self.day18.run(size=12)
        self.assertEqual(expected, actual)
