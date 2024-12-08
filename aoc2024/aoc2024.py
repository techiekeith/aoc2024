import time

from aoc2024.day1 import Day1
from aoc2024.day2 import Day2
from aoc2024.day3 import Day3
from aoc2024.day4 import Day4
from aoc2024.day5 import Day5
from aoc2024.day6 import Day6
from aoc2024.day7 import Day7
from aoc2024.day8 import Day8

days = [Day1(), Day2(), Day3(), Day4(), Day5(), Day6(), Day7(), Day8()]


def run_day(day, day_number):
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


def run():
    for index in range(len(days)):
        run_day(days[index], index + 1)
