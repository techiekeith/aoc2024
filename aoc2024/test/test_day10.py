import unittest
from ..day10 import Day10, find_trailheads, find_next, aggregate_peaks_by_trailhead, count_aggregated_peaks_by_trailhead


class TestDay10(unittest.TestCase):
    def setUp(self):
        self.day10 = Day10()

    def test_load(self):
        self.day10.load("inputs/day10/test_input_1.txt")
        expected = [6,5,4,3,4,5,6]
        actual = self.day10.grid[3]
        self.assertEqual(expected, actual)

    def test_find_trailheads_1(self):
        self.day10.load("inputs/day10/test_input_1.txt")
        expected = [(3,0)]
        actual = find_trailheads(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_find_trailheads_2(self):
        self.day10.load("inputs/day10/test_input_2.txt")
        expected = [(3,0)]
        actual = find_trailheads(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_find_trailheads_3(self):
        self.day10.load("inputs/day10/test_input_3.txt")
        expected = [(1,0),(5,6)]
        actual = find_trailheads(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_find_trailheads_4(self):
        self.day10.load("inputs/day10/test_input_4.txt")
        expected = [(2,0),(4,0),(4,2),(6,4),(2,5),(5,5),(0,6),(6,6),(1,7)]
        actual = find_trailheads(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_find_next(self):
        self.day10.load("inputs/day10/test_input_1.txt")
        expected = [(3,1)]
        actual = find_next(self.day10.grid, (3,0))
        self.assertEqual(expected, actual)

    def test_aggregate_peaks_by_trailhead_1(self):
        self.day10.load("inputs/day10/test_input_1.txt")
        expected = {(0,6):1,(6,6):1}
        actual = aggregate_peaks_by_trailhead(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_aggregate_peaks_by_trailhead_2(self):
        self.day10.load("inputs/day10/test_input_2.txt")
        expected = {(6,0):1,(5,1):1,(4,4):1,(0,6):1}
        actual = aggregate_peaks_by_trailhead(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_aggregate_peaks_by_trailhead_3(self):
        self.day10.load("inputs/day10/test_input_3.txt")
        expected = {(4,0):1,(3,5):2}
        actual = aggregate_peaks_by_trailhead(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_aggregate_peaks_by_trailhead_4(self):
        self.day10.load("inputs/day10/test_input_4.txt")
        expected = {(0,3):5,(1,0):5,(4,3):8,(4,5):5,(4,6):1,(5,2):4,(5,4):8}
        actual = aggregate_peaks_by_trailhead(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_count_aggregated_peaks_by_trailhead_4(self):
        self.day10.load("inputs/day10/test_input_4.txt")
        expected = 36
        actual = count_aggregated_peaks_by_trailhead(self.day10.grid)
        self.assertEqual(expected, actual)

    def test_count_aggregated_peaks_by_trailhead_5(self):
        self.day10.load("inputs/day10/test_input_5.txt")
        expected = 3
        actual = count_aggregated_peaks_by_trailhead(self.day10.grid, count_paths=True)
        self.assertEqual(expected, actual)

    def test_count_aggregated_peaks_by_trailhead_6(self):
        self.day10.load("inputs/day10/test_input_6.txt")
        expected = 13
        actual = count_aggregated_peaks_by_trailhead(self.day10.grid, count_paths=True)
        self.assertEqual(expected, actual)

    def test_count_aggregated_peaks_by_trailhead_7(self):
        self.day10.load("inputs/day10/test_input_7.txt")
        expected = 227
        actual = count_aggregated_peaks_by_trailhead(self.day10.grid, count_paths=True)
        self.assertEqual(expected, actual)

    def test_count_aggregated_peaks_by_trailhead_4_part_2(self):
        self.day10.load("inputs/day10/test_input_4.txt")
        expected = 81
        actual = count_aggregated_peaks_by_trailhead(self.day10.grid, count_paths=True)
        self.assertEqual(expected, actual)
