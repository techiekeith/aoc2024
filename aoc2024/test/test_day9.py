import unittest
from ..day9 import Day9, get_blocks, compact_blocks, compact_files, get_filesystem_checksum


class TestDay9(unittest.TestCase):
    def setUp(self):
        self.day9 = Day9()
        self.day9.load("inputs/day9/test_input.txt")

    def test_load(self):
        expected_disk_map = [2,3,3,3,1,3,3,1,2,1,4,1,4,1,3,1,4,0,2]
        self.assertEqual(expected_disk_map, self.day9.disk_map)

    def test_get_blocks(self):
        disk_map = [2,3,3,3,1,3,3,1,2,1,4,1,4,1,3,1,4,0,2]
        expected_blocks = [0,0,-1,-1,-1,1,1,1,-1,-1,-1,2,-1,-1,-1,3,3,3,-1,4,4,-1,5,5,5,5,-1,6,6,6,6,-1,7,7,7,-1,8,8,8,8,9,9]
        actual_blocks = get_blocks(disk_map)
        self.assertEqual(expected_blocks, actual_blocks)

    def test_compact_blocks(self):
        blocks = [0,0,-1,-1,-1,1,1,1,-1,-1,-1,2,-1,-1,-1,3,3,3,-1,4,4,-1,5,5,5,5,-1,6,6,6,6,-1,7,7,7,-1,8,8,8,8,9,9]
        expected_compacted_blocks = [0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6]
        actual_compacted_blocks = compact_blocks(blocks)
        self.assertEqual(expected_compacted_blocks, actual_compacted_blocks)

    def test_get_filesystem_checksum(self):
        compacted_blocks = [0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6]
        expected_checksum = 1928
        actual_checksum = get_filesystem_checksum(compacted_blocks)
        self.assertEqual(expected_checksum, actual_checksum)

    def test_compact_files(self):
        disk_map = [2,3,3,3,1,3,3,1,2,1,4,1,4,1,3,1,4,0,2]
        expected_compacted_blocks = [0,0,9,9,2,1,1,1,7,7,7,-1,4,4,-1,3,3,3,-1,-1,-1,-1,5,5,5,5,-1,6,6,6,6,-1,-1,-1,-1,-1,8,8,8,8,-1,-1]
        actual_compacted_blocks = compact_files(disk_map)
        self.assertEqual(expected_compacted_blocks, actual_compacted_blocks)
