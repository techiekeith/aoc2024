from aoc2024.day import Day


directions = [(0,-1),(1,0),(0,1),(-1,0)]


def find_trailheads(grid):
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                trailheads.append((x, y))
    return trailheads


def find_next(grid, location):
    next_values = []
    height = grid[location[1]][location[0]]
    for direction in directions:
        nx, ny = location[0] + direction[0], location[1] + direction[1]
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
            new_height = grid[ny][nx]
            if new_height == height + 1:
                next_values.append((nx, ny))
    return next_values


def find_peaks(grid, trailheads):
    peaks = {}
    paths = trailheads[:]
    while len(paths) > 0:
        new_paths = []
        for path in paths:
            if grid[path[1]][path[0]] == 9:
                peaks[path] = peaks.get(path, 0) + 1
            else:
                new_paths += find_next(grid, path)
        paths = new_paths
    return peaks


def find_peaks_for_each_trailhead(grid):
    trailheads = find_trailheads(grid)
    peaks = {}
    for trailhead in trailheads:
        peaks[trailhead] = find_peaks(grid, [trailhead])
    return peaks


def aggregate_peaks_by_trailhead(grid, count_paths=False):
    trailhead_peaks = find_peaks_for_each_trailhead(grid)
    aggregate_peaks = {}
    for trailhead in trailhead_peaks:
        peaks = trailhead_peaks[trailhead]
        for peak in peaks:
            aggregate_peaks[peak] = aggregate_peaks.get(peak, 0) + (peaks[peak] if count_paths else 1)
    return aggregate_peaks


def count_aggregated_peaks_by_trailhead(grid, count_paths=False):
    aggregate_peaks = aggregate_peaks_by_trailhead(grid, count_paths)
    return sum([aggregate_peaks[value] for value in aggregate_peaks])


class Day10(Day):
    grid = None

    def load(self, input_file):
        self.grid = []
        with open(input_file, 'r') as file:
            while line := file.readline():
                self.grid.append([-1 if digit == "."  else int(digit) for digit in line.strip()])

    def part1(self):
        return count_aggregated_peaks_by_trailhead(self.grid)

    def part2(self):
        return count_aggregated_peaks_by_trailhead(self.grid, count_paths=True)
