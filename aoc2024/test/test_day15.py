import unittest

from ..day15 import Day15


class TestDay15(unittest.TestCase):
    def setUp(self):
        self.day15 = Day15()

    def test_load(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        expected_second_row = [char for char in "#..O.O.#"]
        expected_moves = [char for char in "<^^>>>vv<v>>v<<"]
        self.assertEqual(expected_second_row, self.day15.grid[1])
        self.assertEqual(expected_moves, self.day15.moves)

    def test_robot_position(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        self.day15.reset()
        expected_robot_position = (2, 2)
        self.assertEqual(expected_robot_position, self.day15.robot.position)

    def test_robot_position_grid_location(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        self.day15.reset()
        self.assertEqual(".", self.day15.robot.grid[self.day15.robot.position[0]][self.day15.robot.position[1]])

    def test_move_1(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        self.day15.reset()
        self.day15.robot.move()
        expected_robot_position = (2, 2)
        self.assertEqual(expected_robot_position, self.day15.robot.position)

    def test_move_2(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        self.day15.reset()
        self.day15.robot.move(moves=2)
        expected_robot_position = (2, 1)
        self.assertEqual(expected_robot_position, self.day15.robot.position)

    def test_move_all(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        self.day15.reset()
        self.day15.robot.move(all_moves=True)
        expected_robot_position = (4, 4)
        self.assertEqual(expected_robot_position, self.day15.robot.position)

    def test_get_box_locations(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        self.day15.reset()
        self.day15.robot.move(all_moves=True)
        expected_box_locations = [(5, 1), (6, 1), (6, 3), (3, 4), (4, 5), (4, 6)]
        self.assertEqual(expected_box_locations, self.day15.robot.get_box_locations())

    def test_sum_of_all_coordinates(self):
        self.day15.load("inputs/day15/test_input_2.txt")
        self.day15.reset()
        self.day15.robot.move(all_moves=True)
        expected_sum_of_all_coordinates = 2028
        self.assertEqual(expected_sum_of_all_coordinates, self.day15.robot.sum_of_all_coordinates())

    def test_sum_of_all_coordinates_input_1(self):
        self.day15.load("inputs/day15/test_input_1.txt")
        self.day15.reset()
        self.day15.robot.move(all_moves=True)
        expected_sum_of_all_coordinates = 10092
        self.assertEqual(expected_sum_of_all_coordinates, self.day15.robot.sum_of_all_coordinates())

    def test_input_3_wide_move_1(self):
        self.day15.load("inputs/day15/test_input_3.txt")
        self.day15.reset(wide=True)
        expected_row = [char for char in "##...[][]...##"]
        expected_position = (9, 3)
        self.day15.robot.move()
        self.assertEqual(expected_row, self.day15.robot.grid[3])
        self.assertEqual(expected_position, self.day15.robot.position)

    def test_input_3_wide_move_6(self):
        self.day15.load("inputs/day15/test_input_3.txt")
        self.day15.reset(wide=True)
        expected_row_2 = [char for char in "##...[][]...##"]
        expected_row_3 = [char for char in "##....[]....##"]
        expected_position = (7, 4)
        self.day15.robot.move(moves=6)
        self.assertEqual(expected_row_2, self.day15.robot.grid[2])
        self.assertEqual(expected_row_3, self.day15.robot.grid[3])
        self.assertEqual(expected_position, self.day15.robot.position)

    def test_input_3_wide_all_moves(self):
        self.day15.load("inputs/day15/test_input_3.txt")
        self.day15.reset(wide=True)
        expected_row_1 = [char for char in "##...[].##..##"]
        expected_row_2 = [char for char in "##.....[]...##"]
        expected_row_3 = [char for char in "##....[]....##"]
        expected_position = (5, 2)
        self.day15.robot.move(all_moves=True)
        self.assertEqual(expected_row_1, self.day15.robot.grid[1])
        self.assertEqual(expected_row_2, self.day15.robot.grid[2])
        self.assertEqual(expected_row_3, self.day15.robot.grid[3])
        self.assertEqual(expected_position, self.day15.robot.position)

    def test_sum_of_all_coordinates_input_1_wide(self):
        self.day15.load("inputs/day15/test_input_1.txt")
        self.day15.reset(wide=True)
        self.day15.robot.move(all_moves=True)
        expected_sum_of_all_coordinates = 9021
        self.assertEqual(expected_sum_of_all_coordinates, self.day15.robot.sum_of_all_coordinates())
