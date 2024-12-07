from aoc2024.day1 import Day1
from aoc2024.day2 import Day2
from aoc2024.day3 import Day3
from aoc2024.day4 import Day4
from aoc2024.day5 import Day5
from aoc2024.day6 import Day6
from aoc2024.day7 import Day7

days = [Day1(), Day2(), Day3(), Day4(), Day5(), Day6(), Day7()]


def run_day(day, day_number):
    day.load(f"inputs/day{day_number}/input.txt")
    part1 = day.part1()
    print(f"Day {day_number} Part 1: {part1}")
    if day.is_part2_performance_slow():
        part2 = "(slow)"
    else:
        part2 = day.part2()
    print(f"Day {day_number} Part 2: {part2}")


def run():
    for index in range(len(days)):
        run_day(days[index], index + 1)
