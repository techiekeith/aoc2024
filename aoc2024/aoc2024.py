import time

from aoc2024.day1 import Day1
from aoc2024.day10 import Day10
from aoc2024.day11 import Day11
from aoc2024.day12 import Day12
from aoc2024.day13 import Day13
from aoc2024.day14 import Day14
from aoc2024.day2 import Day2
from aoc2024.day3 import Day3
from aoc2024.day4 import Day4
from aoc2024.day5 import Day5
from aoc2024.day6 import Day6
from aoc2024.day7 import Day7
from aoc2024.day8 import Day8
from aoc2024.day9 import Day9

days = [
    Day1(), Day2(), Day3(), Day4(), Day5(), Day6(), Day7(), Day8(), Day9(), Day10(), Day11(), Day12(), Day13(), Day14()
]


def run_day(day_number):
    day = days[day_number - 1]
    day.load(f"inputs/day{day_number}/input.txt")
    part1_start = time.perf_counter()
    part1 = day.part1()
    part1_end = time.perf_counter()
    print(f"Day {day_number} Part 1: {part1} ({part1_end - part1_start:.6f} seconds)")
    part2_start = time.perf_counter()
    if day.is_part2_performance_slow():
        part2 = "(slow)"
    else:
        part2 = day.part2()
    part2_end = time.perf_counter()
    print(f"Day {day_number} Part 2: {part2} ({part2_end - part2_start:.6f} seconds)")


def run(args):
    if len(args) == 0:
        for index in range(len(days)):
            run_day(index + 1)
    else:
        [run_day(int(arg)) for arg in args]
