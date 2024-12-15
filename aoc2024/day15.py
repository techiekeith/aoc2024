import functools

from aoc2024.day import Day


class Robot:
    grid = None
    wide = False
    position = None
    directions = None
    directions_index = 0

    direction_dict = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    def __init__(self, grid, moves, wide):
        self.grid = []
        self.wide = wide
        self.position = None
        for y in range(len(grid)):
            row = []
            for x in range(len(grid[y])):
                cell = grid[y][x]
                if cell == '@':
                    self.position = (x * 2 if wide else x, y)
                    cell = '.'
                if wide:
                    if cell == 'O':
                        cell1 = '['
                        cell2 = ']'
                    else:
                        cell1 = cell
                        cell2 = cell
                    row.append(cell1)
                    row.append(cell2)
                else:
                    row.append(cell)
            self.grid.append(row[:])
        self.directions = [self.direction_dict[key] for key in moves[:]]
        self.directions_index = 0

    def move(self, moves=1, all_moves=False):
        count = 0
        while (all_moves or count < moves) and self.directions_index < len(self.directions):
            count += 1
            direction = self.directions[self.directions_index]
            next_position = (self.position[0] + direction[0], self.position[1] + direction[1])
            self.directions_index += 1
            cell = self.grid[next_position[1]][next_position[0]]
            if cell == 'O':
                self.move_boxes(next_position, direction)
            if cell == '[' or cell == ']':
                self.move_wide_boxes(next_position, direction)
            if self.grid[next_position[1]][next_position[0]] == '.':
                self.position = next_position

    def move_boxes(self, box_position, direction):
        next_position = (box_position[0] + direction[0], box_position[1] + direction[1])
        while self.grid[next_position[1]][next_position[0]] == 'O':
            next_position = (next_position[0] + direction[0], next_position[1] + direction[1])
        if self.grid[next_position[1]][next_position[0]] == '.':
            self.grid[next_position[1]][next_position[0]] = 'O'
            self.grid[box_position[1]][box_position[0]] = '.'

    def move_wide_boxes(self, box_position, direction):
        dx, dy = direction
        if dx == 0:
            x, y = box_position
            if self.grid[y][x] == ']':
                x -= 1
            self.move_wide_boxes_vertical((x, y), dy)
        else:
            self.move_wide_boxes_horizontal(box_position, dx)

    def move_wide_boxes_horizontal(self, box_position, dx):
        x, y = box_position
        nx = x + dx
        while self.grid[y][nx] == '[' or self.grid[y][nx] == ']':
            nx = nx + dx
        if self.grid[y][nx] == '.':
            for sx in range(nx, x, -dx):
                self.grid[y][sx] = self.grid[y][sx - dx]
            self.grid[y][x] = '.'

    def move_wide_boxes_vertical(self, box_position, dy):
        if self.can_move_wide_box_vertical(box_position, dy):
            self.can_move_wide_box_vertical(box_position, dy, perform_move=True)

    def can_move_wide_box_vertical(self, position, dy, perform_move=False):
        x, y = position
        ny = y + dy
        if self.grid[ny][x] == '#' or self.grid[ny][x + 1] == '#':
            return False
        box_positions = []
        for nx in range(x - 1, x + 2):
            if self.grid[ny][nx] == '[':
                box_positions.append((nx, ny))
        results = [True] + [self.can_move_wide_box_vertical(next_box_position, dy, perform_move)
                            for next_box_position in box_positions]
        result = functools.reduce(lambda a, b: a and b, results)
        if perform_move:
            self.grid[ny][x] = '['
            self.grid[ny][x + 1] = ']'
            self.grid[y][x] = '.'
            self.grid[y][x + 1] = '.'
        return result

    def get_box_locations(self):
        box_locations = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 'O' or self.grid[y][x] == '[':
                    box_locations.append((x, y))
        return box_locations

    def sum_of_all_coordinates(self):
        box_locations = self.get_box_locations()
        return sum([position[0] + position[1] * 100 for position in box_locations])


class Day15(Day):
    moves = None
    grid = None
    robot = None

    def load(self, input_file):
        self.grid = []
        self.moves = []
        with open(input_file, 'r') as file:
            loading_moves = False
            while line := file.readline():
                row = line.strip()
                if row == "":
                    loading_moves = True
                    continue
                if loading_moves:
                    self.moves += [char for char in row]
                    continue
                self.grid.append([char for char in row])

    def reset(self, wide=False):
        self.robot = Robot(self.grid, self.moves, wide)

    def part1(self):
        self.reset()
        self.robot.move(all_moves=True)
        return self.robot.sum_of_all_coordinates()

    def part2(self):
        self.reset(wide=True)
        self.robot.move(all_moves=True)
        return self.robot.sum_of_all_coordinates()
