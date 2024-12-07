import unittest
from ..day6 import Day6


class TestDay6(unittest.TestCase):
    def setUp(self):
        self.day6 = Day6()
        self.day6.load("inputs/day6/test_input.txt")

    def test_load(self):
        expected_first_row = [x for x in "....#....."]
        expected_location = (6, 4)
        expected_direction = 0
        self.assertEqual(expected_first_row, self.day6.grid[0])
        self.assertEqual(expected_location, self.day6.location)
        self.assertEqual(expected_direction, self.day6.direction)

    def test_get_next_location_north(self):
        initial_location = (6, 4)
        initial_direction = self.day6.north
        expected_location = (5, 4)
        actual_location = self.day6.get_next_location(initial_location, initial_direction)
        self.assertEqual(expected_location, actual_location)

    def test_get_next_location_east(self):
        initial_location = (6, 4)
        initial_direction = self.day6.east
        expected_location = (6, 5)
        actual_location = self.day6.get_next_location(initial_location, initial_direction)
        self.assertEqual(expected_location, actual_location)

    def test_get_next_location_south(self):
        initial_location = (6, 4)
        initial_direction = self.day6.south
        expected_location = (7, 4)
        actual_location = self.day6.get_next_location(initial_location, initial_direction)
        self.assertEqual(expected_location, actual_location)

    def test_get_next_location_west(self):
        initial_location = (6, 4)
        initial_direction = self.day6.west
        expected_location = (6, 3)
        actual_location = self.day6.get_next_location(initial_location, initial_direction)
        self.assertEqual(expected_location, actual_location)

    def test_get_cell_at_location(self):
        self.assertEqual(".", self.day6.get_cell_at_location((5, 4)))
        self.assertEqual("#", self.day6.get_cell_at_location((0, 4)))
        self.assertIsNone(self.day6.get_cell_at_location((-1, 0)))
        self.assertIsNone(self.day6.get_cell_at_location((10, 0)))

    def test_move_no_obstacle(self):
        start_y = 6
        start_x = 4
        self.day6.location = (start_y, start_x)
        self.day6.direction = self.day6.north
        expected_y = 5
        expected_x = 4
        expected_location = (expected_y, expected_x)
        expected_direction = self.day6.north
        self.day6.move()
        self.assertEqual(expected_location, self.day6.location)
        self.assertEqual(expected_direction, self.day6.direction)

    def test_move_with_obstacle(self):
        start_y = 1
        start_x = 4
        self.day6.location = (start_y, start_x)
        self.day6.direction = self.day6.north
        expected_y = 1
        expected_x = 5
        expected_location = (expected_y, expected_x)
        expected_direction = self.day6.east
        self.day6.move()
        self.assertEqual(expected_location, self.day6.location)
        self.assertEqual(expected_direction, self.day6.direction)

    def test_move_with_obstacle_west_to_north(self):
        start_y = 3
        start_x = 3
        self.day6.location = (start_y, start_x)
        self.day6.direction = self.day6.west
        expected_y = 2
        expected_x = 3
        expected_location = (expected_y, expected_x)
        expected_direction = self.day6.north
        self.day6.move()
        self.assertEqual(expected_location, self.day6.location)
        self.assertEqual(expected_direction, self.day6.direction)

    def test_count_visited_locations(self):
        expected = 41
        actual = len(self.day6.get_visited_locations())
        self.assertEqual(expected, actual)

    def test_count_loops(self):
        expected = 6
        actual = self.day6.count_loops()
        self.assertEqual(expected, actual)
