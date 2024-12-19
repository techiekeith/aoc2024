import unittest

from ..day19 import Day19, count_matches, count_possible_designs, count_design_permutations, memoize_patterns


class TestDay19(unittest.TestCase):
    def setUp(self):
        self.day19 = Day19()

    def test_load(self):
        self.day19.load("inputs/day19/test_input.txt")
        expected_patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        expected_designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
        self.assertEqual(expected_patterns, self.day19.patterns)
        self.assertEqual(expected_designs, self.day19.designs)

    def test_count_matches(self):
        patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        parameters = [
            ("brwrr", 2),
            ("bggr", 1),
            ("gbbr", 4),
            ("rrbgbr", 6),
            ("ubwu", 0),
            ("bwurrg", 1),
            ("brgr", 2),
            ("bbrgwb", 0),
        ]
        for design, expected in parameters:
            with self.subTest(msg=design, design=design, expected=expected):
                memo = memoize_patterns(patterns)
                actual = count_matches(design, patterns, memo)
                self.assertEqual(expected, actual)

    def test_count_possible_designs(self):
        patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
        expected = 6
        memo = memoize_patterns(patterns)
        self.assertEqual(expected, count_possible_designs(designs, patterns, memo))

    def test_count_design_permutations(self):
        patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
        expected = 16
        memo = memoize_patterns(patterns)
        self.assertEqual(expected, count_design_permutations(designs, patterns, memo))
