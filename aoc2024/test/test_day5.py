import unittest
from ..day5 import Day5, order_matches_rule, update_is_ordered, get_ordered_updates, get_middle_value, \
    correct_update_order, get_disordered_updates


class TestDay5(unittest.TestCase):
    def setUp(self):
        self.day5 = Day5()
        self.day5.load("inputs/day5/test_input.txt")

    def test_load_page_ordering_rules(self):
        expected_first_page_ordering_rule = (47, 53)
        expected_last_page_ordering_rule = (53, 13)
        self.assertEqual(1, self.day5.page_ordering_rules.get(expected_first_page_ordering_rule))
        self.assertEqual(21, self.day5.page_ordering_rules.get(expected_last_page_ordering_rule))

    def test_load_updates(self):
        expected_first_update = [75, 47, 61, 53, 29]
        expected_last_update = [97, 13, 75, 29, 47]
        self.assertEqual(expected_first_update, self.day5.updates[0])
        self.assertEqual(expected_last_update, self.day5.updates[-1])

    def test_order_matches_rule(self):
        expected_ordering_rule = (47, 53)
        unexpected_ordering_rule = (53, 12)
        self.assertTrue(order_matches_rule(self.day5.page_ordering_rules, expected_ordering_rule))
        self.assertFalse(order_matches_rule(self.day5.page_ordering_rules, unexpected_ordering_rule))

    def test_update_is_ordered(self):
        self.assertTrue(update_is_ordered(self.day5.page_ordering_rules, self.day5.updates[0]))
        self.assertTrue(update_is_ordered(self.day5.page_ordering_rules, self.day5.updates[1]))
        self.assertTrue(update_is_ordered(self.day5.page_ordering_rules, self.day5.updates[2]))
        self.assertFalse(update_is_ordered(self.day5.page_ordering_rules, self.day5.updates[3]))
        self.assertFalse(update_is_ordered(self.day5.page_ordering_rules, self.day5.updates[4]))
        self.assertFalse(update_is_ordered(self.day5.page_ordering_rules, self.day5.updates[5]))

    def test_get_ordered_updates(self):
        ordered_updates = get_ordered_updates(self.day5.page_ordering_rules, self.day5.updates)
        self.assertEqual(3, len(ordered_updates))
        self.assertEqual(self.day5.updates[0], ordered_updates[0])
        self.assertEqual(self.day5.updates[1], ordered_updates[1])
        self.assertEqual(self.day5.updates[2], ordered_updates[2])

    def test_get_middle_value(self):
        self.assertEqual(5, get_middle_value([1, 3, 5, 7, 9]))

    def test_get_total_middle_values_of_ordered_updates(self):
        self.assertEqual(143, self.day5.get_total_middle_values_of_ordered_updates())

    def test_get_disordered_updates(self):
        disordered_updates = get_disordered_updates(self.day5.page_ordering_rules, self.day5.updates)
        self.assertEqual(3, len(disordered_updates))
        self.assertEqual(self.day5.updates[3], disordered_updates[0])
        self.assertEqual(self.day5.updates[4], disordered_updates[1])
        self.assertEqual(self.day5.updates[5], disordered_updates[2])

    def test_corrected_order(self):
        disordered_update_1 = self.day5.updates[3]
        expected_corrected_update_1 = [97, 75, 47, 61, 53]
        disordered_update_2 = self.day5.updates[4]
        expected_corrected_update_2 = [61, 29, 13]
        disordered_update_3 = self.day5.updates[5]
        expected_corrected_update_3 = [97, 75, 47, 29, 13]
        self.assertEqual(expected_corrected_update_1, correct_update_order(self.day5.page_ordering_rules, disordered_update_1))
        self.assertEqual(expected_corrected_update_2, correct_update_order(self.day5.page_ordering_rules, disordered_update_2))
        self.assertEqual(expected_corrected_update_3, correct_update_order(self.day5.page_ordering_rules, disordered_update_3))

    def test_get_total_middle_values_of_disordered_updates(self):
        self.assertEqual(123, self.day5.get_total_middle_values_of_disordered_updates())
