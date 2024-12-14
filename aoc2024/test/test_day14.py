import unittest

from ..day14 import Day14, Robot, get_robot_positions_after_n_moves, get_safety_factor


class TestDay14(unittest.TestCase):
    def setUp(self):
        self.width = 11
        self.height = 7
        self.day14 = Day14(self.width, self.height)
        self.day14.load("inputs/day14/test_input.txt")

    def test_load(self):
        expected = [
            Robot((0, 4), (3, -3)),
            Robot((6, 3), (-1, -3)),
            Robot((10, 3), (-1, 2)),
            Robot((2, 0), (2, -1)),
            Robot((0, 0), (1, 3)),
            Robot((3, 0), (-2, -2)),
            Robot((7, 6), (-1, -3)),
            Robot((3, 0), (-1, -2)),
            Robot((9, 3), (2, 3)),
            Robot((7, 3), (-1, 2)),
            Robot((2, 4), (2, -3)),
            Robot((9, 5), (-3, -3)),
        ]
        self.assertEqual(expected, self.day14.robots)

    def test_position_after_n_moves(self):
        robot = Robot((2, 4), (2, -3))
        self.assertEqual((4, 1), robot.get_position_after_n_moves(self.width, self.height, 1))
        self.assertEqual((6, 5), robot.get_position_after_n_moves(self.width, self.height, 2))
        self.assertEqual((8, 2), robot.get_position_after_n_moves(self.width, self.height, 3))
        self.assertEqual((10, 6), robot.get_position_after_n_moves(self.width, self.height, 4))
        self.assertEqual((1, 3), robot.get_position_after_n_moves(self.width, self.height, 5))

    def test_robots_after_100_moves(self):
        expected = [
            (3, 5),
            (5, 4),
            (9, 0),
            (4, 5),
            (1, 6),
            (1, 3),
            (6, 0),
            (2, 3),
            (0, 2),
            (6, 0),
            (4, 5),
            (6, 6),
        ]
        self.assertEqual(expected, get_robot_positions_after_n_moves(self.day14.robots, self.width, self.height, 100))

    def test_safety_factor(self):
        positions = get_robot_positions_after_n_moves(self.day14.robots, self.width, self.height, 100)
        expected = 12
        self.assertEqual(expected, get_safety_factor(positions, self.width, self.height))
