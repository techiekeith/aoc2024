import unittest
from ..day12 import Day12, get_region_area_and_perimeter, get_regions, calculate_cost, calculate_discounted_cost


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.day12 = Day12()
        # self.day12.load("inputs/day11/test_input.txt")

    def test_load(self):
        self.day12.load("inputs/day12/test_input_1.txt")

    def test_get_region_area_and_perimeter(self):
        self.day12.load("inputs/day12/test_input_1.txt")
        cells, perimeter = get_region_area_and_perimeter(self.day12.grid, (0, 0))
        self.assertEqual(len(cells), 4)
        self.assertEqual(len(perimeter), 10)

    def test_get_regions_1(self):
        self.day12.load("inputs/day12/test_input_1.txt")
        expected_total_regions = 5
        expected_region_a = { "region": "A", "area": 4, "perimeter": 10, "sides": 4 }
        expected_region_b = { "region": "B", "area": 4, "perimeter": 8, "sides": 4 }
        expected_region_c = { "region": "C", "area": 4, "perimeter": 10, "sides": 8 }
        expected_region_d = { "region": "D", "area": 1, "perimeter": 4, "sides": 4 }
        expected_region_e = { "region": "E", "area": 3, "perimeter": 8, "sides": 4 }
        regions = get_regions(self.day12.grid)
        self.assertEqual(expected_total_regions, len(regions.keys()))
        self.assertEqual(expected_region_a, regions[(0,0)])
        self.assertEqual(expected_region_b, regions[(0,1)])
        self.assertEqual(expected_region_c, regions[(2,1)])
        self.assertEqual(expected_region_d, regions[(3,1)])
        self.assertEqual(expected_region_e, regions[(0,3)])

    def test_get_regions_2(self):
        self.day12.load("inputs/day12/test_input_2.txt")
        expected_total_regions = 5
        expected_region_o = { "region": "O", "area": 21, "perimeter": 36, "sides": 20 }
        expected_region_x = { "region": "X", "area": 1, "perimeter": 4, "sides": 4 }
        regions = get_regions(self.day12.grid)
        self.assertEqual(expected_total_regions, len(regions.keys()))
        self.assertEqual(expected_region_o, regions[(0,0)])
        self.assertEqual(expected_region_x, regions[(1,1)])
        self.assertEqual(expected_region_x, regions[(3,1)])
        self.assertEqual(expected_region_x, regions[(1,3)])
        self.assertEqual(expected_region_x, regions[(3,3)])

    def test_get_regions_3(self):
        self.day12.load("inputs/day12/test_input_3.txt")
        expected_total_regions = 11
        expected_region_r = { "region": "R", "area": 12, "perimeter": 18, "sides": 10 }
        expected_region_i1 = { "region": "I", "area": 4, "perimeter": 8, "sides": 4 }
        expected_region_c1 = { "region": "C", "area": 14, "perimeter": 28, "sides": 22 }
        expected_region_f = { "region": "F", "area": 10, "perimeter": 18, "sides": 12 }
        expected_region_v = { "region": "V", "area": 13, "perimeter": 20, "sides": 10 }
        expected_region_j = { "region": "J", "area": 11, "perimeter": 20, "sides": 12 }
        expected_region_c2 = { "region": "C", "area": 1, "perimeter": 4, "sides": 4 }
        expected_region_e = { "region": "E", "area": 13, "perimeter": 18, "sides": 8 }
        expected_region_i2 = { "region": "I", "area": 14, "perimeter": 22, "sides": 16 }
        expected_region_m = { "region": "M", "area": 5, "perimeter": 12, "sides": 6 }
        expected_region_s = { "region": "S", "area": 3, "perimeter": 8, "sides": 6 }
        regions = get_regions(self.day12.grid)
        self.assertEqual(expected_total_regions, len(regions.keys()))
        self.assertEqual(expected_region_r, regions[(0,0)])
        self.assertEqual(expected_region_i1, regions[(4,0)])
        self.assertEqual(expected_region_c1, regions[(6,0)])
        self.assertEqual(expected_region_f, regions[(8,0)])
        self.assertEqual(expected_region_v, regions[(0,2)])
        self.assertEqual(expected_region_j, regions[(6,3)])
        self.assertEqual(expected_region_c2, regions[(7,4)])
        self.assertEqual(expected_region_e, regions[(9,4)])
        self.assertEqual(expected_region_i2, regions[(2,5)])
        self.assertEqual(expected_region_m, regions[(0,7)])
        self.assertEqual(expected_region_s, regions[(4,8)])

    def test_calculate_cost_1(self):
        self.day12.load("inputs/day12/test_input_1.txt")
        expected_cost = 140
        self.assertEqual(expected_cost, calculate_cost(self.day12.grid))

    def test_calculate_cost_2(self):
        self.day12.load("inputs/day12/test_input_2.txt")
        expected_cost = 772
        self.assertEqual(expected_cost, calculate_cost(self.day12.grid))

    def test_calculate_cost_3(self):
        self.day12.load("inputs/day12/test_input_3.txt")
        expected_cost = 1930
        self.assertEqual(expected_cost, calculate_cost(self.day12.grid))

    def test_calculate_discounted_cost_1(self):
        self.day12.load("inputs/day12/test_input_1.txt")
        expected_discounted_cost = 80
        self.assertEqual(expected_discounted_cost, calculate_discounted_cost(self.day12.grid))

    def test_calculate_discounted_cost_2(self):
        self.day12.load("inputs/day12/test_input_2.txt")
        expected_discounted_cost = 436
        self.assertEqual(expected_discounted_cost, calculate_discounted_cost(self.day12.grid))

    def test_calculate_discounted_cost_3(self):
        self.day12.load("inputs/day12/test_input_3.txt")
        expected_discounted_cost = 1206
        self.assertEqual(expected_discounted_cost, calculate_discounted_cost(self.day12.grid))

    def test_calculate_discounted_cost_4(self):
        self.day12.load("inputs/day12/test_input_4.txt")
        expected_discounted_cost = 236
        self.assertEqual(expected_discounted_cost, calculate_discounted_cost(self.day12.grid))

    def test_calculate_discounted_cost_5(self):
        self.day12.load("inputs/day12/test_input_5.txt")
        expected_discounted_cost = 368
        self.assertEqual(expected_discounted_cost, calculate_discounted_cost(self.day12.grid))
