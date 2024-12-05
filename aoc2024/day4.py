from aoc2024.day import Day


class Day4(Day):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def __init__(self):
        self.rows = None

    def load(self, input_file):
        self.rows = []
        with open(input_file, 'r') as file:
            while line := file.readline():
                self.rows.append([char for char in line.strip()])

    def find_starting_positions(self, word, letter_index = 0):
        starting_positions = []
        starting_letter = word[letter_index]
        for row in range(len(self.rows)):
            for column in range(len(self.rows[row])):
                if self.rows[row][column] == starting_letter:
                    starting_positions.append((row, column))
        return starting_positions

    def word_search_from_starting_position(self, word, starting_position, letter_index = 0, diagonal_only = False):
        matches = 0
        (row, column) = starting_position
        for (dy, dx) in self.directions:
            if diagonal_only and (dx == 0 or dy == 0):
                continue
            start_y = row - dy * letter_index
            start_x = column - dx * letter_index
            end_y = start_y + dy * (len(word) - 1)
            end_x = start_x + dx * (len(word) - 1)
            if (self.position_is_in_bounds((start_y, start_x))
                    and self.position_is_in_bounds((end_y, end_x))
                    and self.word_matches_position_and_direction(word, (start_y, start_x), (dy, dx))):
                matches += 1
        return matches

    def position_is_in_bounds(self, position):
        (row, column) = position
        return 0 <= row < len(self.rows) and 0 <= column < len(self.rows[row])

    def word_matches_position_and_direction(self, word, position, direction):
        (row, column) = position
        (dy, dx) = direction
        for index in range(len(word)):
            y = row + dy * index
            x = column + dx * index
            if self.rows[y][x] != word[index]:
                return False
        return True

    def count_all_word_matches(self, word):
        return sum([self.word_search_from_starting_position(word, position) for position in self.find_starting_positions(word)])

    def count_all_cross_matches(self, word):
        letter_index = int(len(word) / 2)
        cross_matches = 0
        for position in self.find_starting_positions(word, letter_index):
            if self.word_search_from_starting_position(word, position, letter_index, True) == 2:
                cross_matches += 1
        return cross_matches

    def part1(self):
        return self.count_all_word_matches("XMAS")

    def part2(self):
        return self.count_all_cross_matches("MAS")
