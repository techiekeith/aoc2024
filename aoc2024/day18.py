import math

from aoc2024.day import Day


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class PathNotFoundException(Exception):
    pass


class Day18(Day):
    def __init__(self, size=70):
        super().__init__()
        self.size = size
        self.corrupted_bytes = []

    def load(self, input_file):
        self.corrupted_bytes = []
        with open(input_file) as f:
            while line := f.readline():
                coords = [int(field.strip()) for field in line.split(',')]
                self.corrupted_bytes.append((coords[0], coords[1]))

    def get_corrupted_bytes_dict(self, start=0, size=1024, corrupted_bytes_dict=None):
        dict_size = min(size, len(self.corrupted_bytes))
        if corrupted_bytes_dict is None:
            corrupted_bytes_dict = {}
        for index in range(start, dict_size):
            corrupted_bytes_dict[self.corrupted_bytes[index]] = 1
        return corrupted_bytes_dict

    def find_next_paths(self, corrupted_bytes_dict=None, paths=None, visited_dict=None):
        if corrupted_bytes_dict is None:
            corrupted_bytes_dict = {}
        if paths is None:
            paths = [(0, 0)]
        if visited_dict is None:
            visited_dict = {}
        next_paths = []
        for path in paths:
            if visited_dict.get(path) is not None:
                continue
            visited_dict[path] = 1
            x, y = path
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                next_location = (nx, ny)
                if (0 <= nx <= self.size
                        and 0 <= ny <= self.size
                        and corrupted_bytes_dict.get(next_location) is None
                        and visited_dict.get(next_location) is None):
                    next_paths.append(next_location)
        return next_paths, visited_dict

    def run(self, size=1024):
        corrupted_bytes_dict = self.get_corrupted_bytes_dict(size=size)
        paths = None
        visited_dict = None
        score = 0
        found = False
        while not found:
            paths, visited_dict = self.find_next_paths(corrupted_bytes_dict=corrupted_bytes_dict, paths=paths, visited_dict=visited_dict)
            if len(paths) == 0:
                raise PathNotFoundException("No paths found")
            score += 1
            for x, y in paths:
                if x == self.size and y == self.size:
                    found = True
        return score

    def find_blocking_byte(self):
        size = len(self.corrupted_bytes)
        section = math.ceil(size / 2)
        while section > 0:
            try:
                self.run(size=size)
                size += section
            except PathNotFoundException:
                size -= section
            section = 0 if section == 1 else math.ceil(section / 2)
        try:
            self.run(size=size)
        except PathNotFoundException:
            size -= 1
        return self.corrupted_bytes[size]

    def part1(self):
        return self.run()

    def part2(self):
        return self.find_blocking_byte()
