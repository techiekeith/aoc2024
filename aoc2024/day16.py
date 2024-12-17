from aoc2024.day import Day


def can_move(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] != "#"


def can_go_forward(grid, location):
    x, y = location.position
    dx, dy = location.direction
    return can_move(grid, x + dx, y + dy)


def can_go_left(grid, location):
    if location.rotated:
        return False
    x, y = location.position
    dx, dy = location.direction
    return can_move(grid, x + dy, y - dx)


def can_go_right(grid, location):
    if location.rotated:
        return False
    x, y = location.position
    dx, dy = location.direction
    return can_move(grid, x - dy, y + dx)


def rotate_left(location):
    dx, dy = location.direction
    return Location(location.position, (dy, -dx), location.score + 1000, rotated=True)


def rotate_right(location):
    dx, dy = location.direction
    return Location(location.position, (-dy, dx), location.score + 1000, rotated=True)


def move(location):
    x, y = location.position
    dx, dy = location.direction
    return Location((x + dx, y + dy), location.direction, location.score + 1)


class Location:
    def __init__(self, position, direction=(1, 0), score=0, start=False, rotated=False):
        self.position = position
        self.direction = direction
        self.score = score
        self.rotated = rotated
        self.start = start
        self.end = False
        self.seat = False

    def __eq__(self, other):
        return (self.position == other.position
                and self.direction == other.direction
                and self.score == other.score
                and self.rotated == other.rotated
                and self.start == other.start
                and self.end == other.end)

    def __repr__(self):
        return f"(x, y)={self.position} (dx, dy)={self.direction} score={self.score} rotated={self.rotated} start={self.start} end={self.end}"


class Day16(Day):
    grid = None
    start = None
    end = None

    def load(self, input_file):
        self.grid = []
        with open(input_file, 'r') as file:
            while line := file.readline():
                self.grid.append([char for char in line.strip()])

    def find_start(self):
        self.start = None
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 'S':
                    self.start = (x, y)
        if self.start is None:
            raise Exception("No start position")

    def find_end(self):
        self.end = None
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 'E':
                    self.end = (x, y)
        if self.end is None:
            raise Exception("No end position")

    def reset(self):
        self.find_start()
        self.find_end()

    def find_next_paths(self, paths=None, visited=None):
        if paths is None:
            paths = [Location(self.start, start=True)]
        if visited is None:
            visited = {}
        next_paths = []
        lowest_score = paths[len(paths) - 1].score
        next_index = 0
        for path_index in range(len(paths)):
            path = paths[path_index]
            if visited.get((path.position, path.direction)) is not None:
                continue
            if path.score > lowest_score:
                next_paths += paths[path_index:]
                break
            visited[(path.position, path.direction)] = path
            if path.end:
                continue
            if can_go_forward(self.grid, path):
                next_paths += [move(path)]
            if can_go_left(self.grid, path):
                next_paths += [rotate_left(path)]
            if can_go_right(self.grid, path):
                next_paths += [rotate_right(path)]
            for next_path in next_paths[next_index:]:
                if next_path.position == self.end:
                    next_path.end = True
                if lowest_score is None or next_path.score < lowest_score:
                    lowest_score = next_path.score
            next_index = len(next_paths)
        paths = sorted(next_paths, key=lambda x: x.score)
        return paths, visited

    def run(self, full=False):
        self.reset()
        paths = None
        visited = None
        score = -1
        while score < 0 or (full and len(paths) > 0):
            paths, visited = self.find_next_paths(paths, visited)
            for path_index in range(len(paths)):
                if paths[path_index].end is True and score < 0 or score > paths[path_index].score:
                    score = paths[path_index].score
                    break
        return score, visited

    def find_seats(self):
        optimal_score, visited = self.run(full=True)
        paths = []
        for position, direction in visited:
            if position == self.end and visited[(position, direction)].score == optimal_score:
                paths += [(position, direction)]
                visited[(position, direction)].seat = True
        while len(paths) > 0:
            next_paths = []
            for path in paths:
                x, y = path[0]
                dx, dy = path[1]
                back = ((x - dx, y - dy), (dx, dy))
                if visited.get(back) is not None and visited[back].score == visited[path].score - 1:
                    next_paths += [back]
                    visited[back].seat = True
                left = ((x, y), (dy, -dx))
                if visited.get(left) is not None and visited[left].score == visited[path].score - 1000:
                    next_paths += [left]
                    visited[left].seat = True
                right = ((x, y), (-dy, dx))
                if visited.get(right) is not None and visited[right].score == visited[path].score - 1000:
                    next_paths += [right]
                    visited[right].seat = True
            paths = next_paths
        seats = {}
        for position, direction in visited:
            if visited[(position, direction)].seat is True:
                seats[position] = 1
        return len(seats)

    def part1(self):
        optimal_score, visited = self.run()
        return optimal_score

    def part2(self):
        return self.find_seats()
