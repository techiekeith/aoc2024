import math

from aoc2024.day import Day


def get_robot_positions_after_n_moves(robots, width, height, moves):
    return [robot.get_position_after_n_moves(width, height, moves) for robot in robots]


def get_safety_factor(positions, width, height):
    quadrants = [0, 0, 0, 0]
    for position in positions:
        x, y = position[0] - width // 2, position[1] - height // 2
        if x != 0 and y != 0:
            quadrant = (1 if x > 0 else 0) + (2 if y > 0 else 0)
            quadrants[quadrant] += 1
    return math.prod(quadrants)


def calculate_robot_density(robots, width, height, moves):
    positions = {}
    for position in get_robot_positions_after_n_moves(robots, width, height, moves):
        positions[position] = positions.get(position, 0) + 1
    for position in positions.keys():
        # Weight positions by number of adjacent robots
        positions[position] += positions.get((position[0], position[1] - 1), 0)
        positions[position] += positions.get((position[0] + 1, position[1]), 0)
        positions[position] += positions.get((position[0], position[1] + 1), 0)
        positions[position] += positions.get((position[0] - 1, position[1]), 0)
    return sum(positions.values())


def find_tree(robots, width, height):
    densities = {}
    for moves in range(max(width, height)):
        densities[moves] = calculate_robot_density(robots, width, height, moves)
    first, second = sorted(densities.keys(), key=lambda x: densities[x], reverse=True)[:2]
    first_plus_height = calculate_robot_density(robots, width, height, first + height)
    first_plus_width = calculate_robot_density(robots, width, height, first + width)
    second_plus_height = calculate_robot_density(robots, width, height, second + height)
    second_plus_width = calculate_robot_density(robots, width, height, second + width)
    first_step = height if first_plus_height > first_plus_width else width
    second_step = height if second_plus_height > second_plus_width else width
    if first_step == second_step:
        raise Exception("Cannot determine steps to take to find target frame.")
    for moves in range(first, width * height, first_step):
        if (moves - second) % second_step == 0:
            return moves
    raise Exception("Cannot find target frame.")


class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return f"p={self.position}, v={self.velocity}"

    def __eq__(self, other):
        return self.position == other.position and self.velocity == other.velocity

    def get_position_after_n_moves(self, width, height, moves):
        return (
            (self.position[0] + moves * self.velocity[0]) % width,
            (self.position[1] + moves * self.velocity[1]) % height)


class Day14(Day):
    robots = None

    def __init__(self, width=101, height=103):
        self.width = width
        self.height = height

    def load(self, input_file):
        self.robots = []
        with open(input_file, 'r') as file:
            while line := file.readline():
                fields = line.split()
                coords = [[int(a) for a in coords.split(",")] for coords in [field.split("=")[1] for field in fields]]
                p = (coords[0][0], coords[0][1])
                v = (coords[1][0], coords[1][1])
                self.robots.append(Robot(p, v))

    def part1(self):
        positions = get_robot_positions_after_n_moves(self.robots, self.width, self.height, 100)
        return get_safety_factor(positions, self.width, self.height)

    def part2(self):
        return find_tree(self.robots, self.width, self.height)
