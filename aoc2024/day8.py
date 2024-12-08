from aoc2024.day import Day


def find_antinodes(max_x, max_y, coordinates, existing_antinodes=None, repeat=False):
    if existing_antinodes is None:
        existing_antinodes = {}
    antinodes = existing_antinodes
    for index in range(len(coordinates) - 1):
        for next_index in range(index + 1, len(coordinates)):
            ax1, ay1 = coordinates[index]
            ax2, ay2 = coordinates[next_index]
            if repeat:
                antinodes[(ax1, ay1)] = antinodes.get((ax1, ay1), 0) + 1
                antinodes[(ax2, ay2)] = antinodes.get((ax2, ay2), 0) + 1
            dx, dy = ax2 - ax1, ay2 - ay1
            x1, y1 = ax1 - dx, ay1 - dy
            while 0 <= x1 < max_x and 0 <= y1 < max_y:
                antinodes[(x1, y1)] = antinodes.get((x1, y1), 0) + 1
                if not repeat:
                    break
                x1, y1 = x1 - dx, y1 - dy
            x2, y2 = ax2 + dx, ay2 + dy
            while 0 <= x2 < max_x and 0 <= y2 < max_y:
                antinodes[(x2, y2)] = antinodes.get((x2, y2), 0) + 1
                if not repeat:
                    break
                x2, y2 = x2 + dx, y2 + dy
    return antinodes

class Day8(Day):
    antennae = None
    x = None
    y = None

    def load(self, input_file):
        self.antennae = {}
        with open(input_file, 'r') as file:
            self.y = 0
            while line := file.readline():
                row = line.strip()
                self.x = 0
                for char in row:
                    if "0" <= char <= "9" or "A" <= char <= "Z" or "a" <= char <= "z":
                        if char not in self.antennae:
                            self.antennae[char] = []
                        self.antennae[char].append((self.x, self.y))
                    self.x += 1
                self.y += 1

    def count_antinodes(self, repeat=False):
        antinodes = {}
        for char in self.antennae:
            antinodes = find_antinodes(self.x, self.y, self.antennae[char], antinodes, repeat)
        return len(antinodes)

    def part1(self):
        return self.count_antinodes()

    def part2(self):
        return self.count_antinodes(repeat=True)
