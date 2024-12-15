from aoc2024.day import Day


def get_blocks(disk_map):
    blocks = []
    free_space = False
    file_id = 0
    for length in disk_map:
        if free_space:
            blocks += [-1] * length
        else:
            blocks += [file_id] * length
            file_id += 1
        free_space = not free_space
    return blocks


def compact_blocks(blocks):
    compacted_blocks = []
    index = 0
    last_index = len(blocks) - 1
    while blocks[last_index] == -1:
        last_index -= 1
    while index <= last_index:
        block = blocks[index]
        if block == -1:
            block = blocks[last_index]
            last_index -= 1
            while blocks[last_index] == -1:
                last_index -= 1
        compacted_blocks.append(block)
        index += 1
    return compacted_blocks


def compact_files(disk_map):
    blocks = get_blocks(disk_map)
    last_index = len(blocks) - 1
    while last_index > 0:
        block = blocks[last_index]
        if block > 0:
            file_length = disk_map[block * 2]
            free_block = find_index_of_free_block_satisfying_file_length(blocks, last_index, file_length)
            if free_block >= 0:
                for index in range(file_length):
                    blocks[free_block + index] = block
                    blocks[last_index - index] = -1
            last_index -= file_length # skip backward past file
            last_index -= disk_map[block * 2 - 1] # skip backward past free space (if any)
        else:
            last_index = 0
    return blocks


def find_index_of_free_block_satisfying_file_length(blocks, last_index, file_length):
    start_free_block_scan = 0
    while start_free_block_scan < last_index:
        free_space_start = blocks.index(-1, start_free_block_scan)
        if free_space_start >= last_index:
            return -1
        free_space_end = free_space_start + 1
        while blocks[free_space_end] == -1:
            free_space_end += 1
        if free_space_end - free_space_start >= file_length:
            return free_space_start
        start_free_block_scan = free_space_end + 1
    return -1


def get_filesystem_checksum(compacted_blocks):
    return sum([index * compacted_blocks[index] for index in range(len(compacted_blocks)) if compacted_blocks[index] > 0])


class Day9(Day):
    disk_map = None

    def load(self, input_file):
        self.disk_map = []
        with open(input_file, 'r') as file:
            self.disk_map = [int(digit) for digit in file.read().strip()]

    def part1(self):
        return get_filesystem_checksum(compact_blocks(get_blocks(self.disk_map)))

    def part2(self):
        return get_filesystem_checksum(compact_files(self.disk_map))

    def is_part2_performance_slow(self):
        return True
