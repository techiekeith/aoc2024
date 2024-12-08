import re

from aoc2024.day import Day


class Day6(Day):
    direction_transforms = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    north = 0
    east = 1
    south = 2
    west = 3
    move_ok = 0
    move_end = 1
    move_loop = 2

    initial_grid = None
    initial_location = None
    initial_direction = None
    grid = None
    location = None
    direction = None

    def load(self, input_file):
        self.grid = []
        self.initial_location = None
        self.initial_direction = None
        with open(input_file, 'r') as file:
            line_number = 0
            while line := file.readline():
                self.grid.append([x for x in line.strip()])
                match = re.search(r"[\^>v<]", line)
                if match is not None:
                    self.initial_location = (line_number, match.start())
                    self.initial_direction = "^>v<".index(match.group())
                line_number += 1
        self.location = self.initial_location
        self.direction = self.initial_direction

    def get_next_location(self, location, direction):
        (y, x) = location
        (dy, dx) = self.direction_transforms[direction]
        return y + dy, x + dx

    def get_cell_at_location(self, location):
        (y, x) = location
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[y]):
            return self.grid[y][x]
        return None

    def move(self):
        next_location = self.get_next_location(self.location, self.direction)
        while self.get_cell_at_location(next_location) == '#':
            self.direction += 1
            self.direction %= 4
            next_location = self.get_next_location(self.location, self.direction)
        (y, x) = next_location
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[y]):
            self.location = next_location
            return self.move_ok
        self.location = None
        return self.move_end

    def get_visited_locations(self):
        self.location = self.initial_location
        self.direction = self.initial_direction
        visited_locations = {self.location: 1}
        while self.move() == self.move_ok:
            visited_locations[self.location] = 1
        return visited_locations

    def count_loops(self):
        visited_locations = self.get_visited_locations()
        loops = 0

        for visited_location in visited_locations.keys():
            if visited_location != self.initial_location:
                self.grid[visited_location[0]][visited_location[1]] = '#'
                self.location = self.initial_location
                self.direction = self.initial_direction
                path = {}
                result = self.move_ok
                while result == self.move_ok:
                    if (self.location, self.direction) in path:
                        result = self.move_loop
                    else:
                        path[(self.location, self.direction)] = 1
                        result = self.move()
                if result == self.move_loop:
                    loops += 1
                self.grid[visited_location[0]][visited_location[1]] = '.'
        return loops

    def part1(self):
        return len(self.get_visited_locations())

    def part2(self):
        return self.count_loops()

    def is_part2_performance_slow(self):
        return True
