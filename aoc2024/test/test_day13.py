import unittest
from ..day13 import Day13, Machine, find_possible_solutions, find_optimal_prize, find_best_token_cost, find_quicker_solution


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

    def test_find_possible_solutions_1(self):
        machine = self.day13.machines[0]
        expected = [(80, 40, 280)]
        actual = find_possible_solutions(machine)
        self.assertEqual(expected, actual)

    def test_find_possible_solutions_2(self):
        machine = self.day13.machines[1]
        expected = []
        actual = find_possible_solutions(machine)
        self.assertEqual(expected, actual)

    def test_find_possible_solutions_3(self):
        machine = self.day13.machines[2]
        expected = [(38, 86, 200)]
        actual = find_possible_solutions(machine)
        self.assertEqual(expected, actual)

    def test_find_possible_solutions_4(self):
        machine = self.day13.machines[3]
        expected = []
        actual = find_possible_solutions(machine)
        self.assertEqual(expected, actual)

    def test_find_optimal_prize(self):
        solutions = [(1, 2, 5), (2, 0, 6)]
        expected = (1, 2, 5)
        actual = find_optimal_prize(solutions)
        self.assertEqual(expected, actual)

    def test_find_optimal_prize_none(self):
        solutions = []
        expected = (0, 0, 0)
        actual = find_optimal_prize(solutions)
        self.assertEqual(expected, actual)

    def test_find_best_token_cost(self):
        expected = 480
        actual = find_best_token_cost(self.day13.machines)
        self.assertEqual(expected, actual)

    def test_find_quicker_solution_1(self):
        machine = self.day13.machines[0]
        expected = [(80, 40, 280)]
        actual = find_quicker_solution(machine)
        self.assertEqual(expected, actual)

    def test_find_quicker_solution_3(self):
        machine = self.day13.machines[2]
        expected = [(38, 86, 200)]
        actual = find_quicker_solution(machine)
        self.assertEqual(expected, actual)
