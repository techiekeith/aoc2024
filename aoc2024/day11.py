from aoc2024.day import Day


def blink(stones, times=1):
    new_stones = stones
    for iteration in range(times):
        original_stones = new_stones
        new_stones = {}
        for stone in original_stones:
            if stone == 0:
                new_stones[1] = new_stones.get(1, 0) + original_stones[0]
                continue
            str = f"{stone}"
            if len(str) % 2 == 0:
                half = len(str) // 2
                lhs = int(str[:half])
                rhs = int(str[half:])
                new_stones[lhs] = new_stones.get(lhs, 0) + original_stones[stone]
                new_stones[rhs] = new_stones.get(rhs, 0) + original_stones[stone]
            else:
                new_value = stone * 2024
                new_stones[new_value] = new_stones.get(new_value, 0) + original_stones[stone]
    return sum([new_stones[stone] for stone in new_stones])


class Day11(Day):
    stones = None

    def load(self, input_file):
        self.stones = {}
        with open(input_file, 'r') as file:
            stones = [int(value) for value in file.read().split()]
            for stone in stones:
                self.stones[stone] = self.stones.get(stone, 0) + 1

    def part1(self):
        return blink(self.stones, 25)

    def part2(self):
        return blink(self.stones, 75)
