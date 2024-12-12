from aoc2024.day import Day


directions = [(0,-1),(1,0),(0,1),(-1,0)]


def get_next_locations(grid, region, start, visited):
    next_locations = []
    perimeter_locations = []
    x, y = start
    for i in range(len(directions)):
        dy, dx = directions[i]
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == region:
            if (nx, ny) not in visited:
                next_locations.append((nx, ny))
                visited[(nx, ny)] = 1
        else:
            perimeter_locations.append((x, y, i))
    return next_locations, perimeter_locations, visited


def get_region_area_and_perimeter(grid, start):
    region = grid[start[1]][start[0]]
    region_locations = [start]
    perimeter_locations = []
    visited = {start:1}
    visited_index = 0
    length = 1
    while length > visited_index:
        for location in region_locations[visited_index:length]:
            extra_locations, extra_perimeter_locations, visited = get_next_locations(grid, region, location, visited)
            region_locations += extra_locations
            perimeter_locations += extra_perimeter_locations
        visited_index = length
        length = len(region_locations)
    return region_locations, perimeter_locations


def get_regions(grid):
    regions = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] is not None:
                location = (x, y)
                region_locations, perimeter_locations = get_region_area_and_perimeter(grid, location)
                regions[location] = {
                    "region": grid[y][x],
                    "area": len(region_locations),
                    "perimeter": len(perimeter_locations),
                    "sides": get_sides(perimeter_locations),
                }
                for location in region_locations:
                    grid[location[1]][location[0]] = None
    return regions


def get_sides(perimeter_locations):
    sides = {}
    keys = perimeter_locations[:]
    for key in keys:
        sides[key] = 1
    for key in keys:
        if sides[key] is not None:
            x, y, d = key
            if d % 2 == 0:
                index = 1
                while (x, y - index, d) in sides:
                    sides[(x, y - index, d)] = None
                    index += 1
                index = 1
                while (x, y + index, d) in sides:
                    sides[(x, y + index, d)] = None
                    index += 1
            else:
                index = 1
                while (x - index, y, d) in sides:
                    sides[(x - index, y, d)] = None
                    index += 1
                index = 1
                while (x + index, y, d) in sides:
                    sides[(x + index, y, d)] = None
                    index += 1
    return len([x for x in sides.values() if x is not None])

def calculate_cost(grid):
    regions = get_regions(grid)
    return sum([regions[location]["area"] * regions[location]["perimeter"] for location in regions])

def calculate_discounted_cost(grid):
    regions = get_regions(grid)
    return sum([regions[location]["area"] * regions[location]["sides"] for location in regions])


class Day12(Day):
    initial_grid = None
    grid = None

    def load(self, input_file):
        self.initial_grid = []
        with open(input_file, 'r') as file:
            while line := file.readline():
                self.initial_grid.append([char for char in line.strip()])
        self.reset()

    def reset(self):
        self.grid = []
        for row in self.initial_grid:
            self.grid.append(row[:])

    def part1(self):
        self.reset()
        return calculate_cost(self.grid)

    def part2(self):
        self.reset()
        return calculate_discounted_cost(self.grid)
