from aoc2024.day1 import Day1
from aoc2024.day2 import Day2
from aoc2024.day3 import Day3
from aoc2024.day4 import Day4


days = [Day1(), Day2(), Day3(), Day4()]


def run_day(day, day_number):
    day.load(f"inputs/day{day_number}/input.txt")
    part1 = day.part1()
    print(f"Day {day_number} Part 1: {part1}")
    part2 = day.part2()
    print(f"Day {day_number} Part 2: {part2}")


def run():
    for index in range(len(days)):
        run_day(days[index], index + 1)
