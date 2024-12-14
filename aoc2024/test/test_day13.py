import unittest
from ..day13 import Day13, Machine, find_best_token_cost, find_solution


class TestDay13(unittest.TestCase):
    def setUp(self):
        self.day13 = Day13()
        self.day13.load("inputs/day13/test_input.txt")

    def test_load(self):
        expected = [
            Machine(a=(94, 34), b=(22, 67), p=(8400, 5400)),
            Machine(a=(26, 66), b=(67, 21), p=(12748, 12176)),
            Machine(a=(17, 86), b=(84, 37), p=(7870, 6450)),
            Machine(a=(69, 23), b=(27, 71), p=(18641, 10279)),
        ]
        actual = self.day13.machines
        self.assertEqual(expected, actual)

    def test_find_solution_1(self):
        machine = self.day13.machines[0]
        expected = (80, 40, 280)
        actual = find_solution(machine)
        self.assertEqual(expected, actual)

    def test_find_solution_2(self):
        machine = self.day13.machines[1]
        expected = None
        actual = find_solution(machine)
        self.assertEqual(expected, actual)

    def test_find_solution_3(self):
        machine = self.day13.machines[2]
        expected = (38, 86, 200)
        actual = find_solution(machine)
        self.assertEqual(expected, actual)

    def test_find_solution_4(self):
        machine = self.day13.machines[3]
        expected = None
        actual = find_solution(machine)
        self.assertEqual(expected, actual)

    def test_find_best_token_cost(self):
        expected = 480
        actual = find_best_token_cost(self.day13.machines)
        self.assertEqual(expected, actual)
