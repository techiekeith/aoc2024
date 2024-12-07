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

    def reset_grid(self):
        self.grid = [[cell for cell in row] for row in self.initial_grid]
        self.location = self.initial_location
        self.direction = self.initial_direction

    def load(self, input_file):
        self.initial_grid = []
        self.grid = []
        self.location = None
        self.direction = None
        with open(input_file, 'r') as file:
            line_number = 0
            while line := file.readline():
                self.initial_grid.append([x for x in line.strip()])
                match = re.search(r"[\^>v<]", line)
                if match is not None:
                    self.initial_location = (line_number, match.start())
                    self.initial_direction = "^>v<".index(match.group())
                line_number += 1
        self.reset_grid()

    def get_next_location(self, location, direction):
        (y, x) = location
        (dy, dx) = self.direction_transforms[direction]
        return y + dy, x + dx

    def get_cell_at_location(self, location):
        (y, x) = location
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[y]):
            return self.grid[y][x]
        return None

    def set_cell_at_location(self, location, direction):
        (y, x) = location
        cell_value = "^>v<"[direction]
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[y]):
            if self.grid[y][x] == cell_value:
                return self.move_loop
            if self.grid[y][x] == "#" or self.grid[y][x] == "O":
                raise Exception(f"Illegal set-cell operation at {location} {direction}")
            self.grid[y][x] = cell_value
            return self.move_ok
        return self.move_end

    def check_for_obstacle(self, location, direction):
        next_cell = self.get_cell_at_location(self.get_next_location(location, direction))
        return next_cell == '#' or next_cell == 'O'

    def move(self):
        while self.check_for_obstacle(self.location, self.direction):
            self.direction += 1
            self.direction %= 4
        self.location = self.get_next_location(self.location, self.direction)
        return self.set_cell_at_location(self.location, self.direction)

    def count_visited_locations(self):
        self.reset_grid()
        while self.move() == self.move_ok:
            pass
        visited_locations = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != '#' and self.grid[y][x] != '.':
                    visited_locations += 1
        return visited_locations

    def count_loops(self):
        self.count_visited_locations()
        visited_grid = [[cell for cell in row] for row in self.grid]
        loops = 0
        for y in range(len(self.grid)):
            print(f"Processing row {y + 1} / {len(self.grid)}")
            for x in range(len(self.grid[y])):
                if visited_grid[y][x] != '#' and visited_grid[y][x] != '.': # only place obstacles in visited locations
                    self.reset_grid()
                    if self.grid[y][x] == '.': # don't place an obstacle in starting location
                        self.grid[y][x] = 'O'
                        result = self.move_ok
                        while result == self.move_ok:
                            result = self.move()
                        if result == self.move_loop:
                            loops += 1
        return loops

    def part1(self):
        return self.count_visited_locations()

    def part2(self):
        return self.count_loops()
