from aoc2024.day import Day


def detect_error(report):
    is_ascending = report[1] > report[0]
    for i in range(1, len(report)):
        difference = report[i] - report[i-1]
        if difference < 0 and is_ascending:
            return i
        if difference > 0 and not is_ascending:
            return i
        difference = abs(difference)
        if difference == 0 or difference > 3:
            return i
    return -1


def is_report_safe(report):
    return detect_error(report) < 0


def is_report_mostly_safe(report):
    error_index = detect_error(report)
    if error_index == -1:
        return True
    skip_first = report[:error_index - 1] + report[error_index:]
    result = is_report_safe(skip_first)
    if not result:
        skip_second = report[:error_index] + report[error_index + 1:]
        result = is_report_safe(skip_second)
    if not result and error_index > 1:
        skip_prev = report[:error_index - 2] + report[error_index - 1:]
        result = is_report_safe(skip_prev)
    return result


class Day2(Day):
    def __init__(self):
        self.reports = None

    def load(self, input_file):
        self.reports = []
        with open(input_file, 'r') as file:
            while line := file.readline():
                sequence = [int(field) for field in line.split()]
                self.reports.append(sequence)

    def count_safe_reports(self):
        safe_reports = 0
        for report in self.reports:
            if is_report_safe(report):
                safe_reports += 1
        return safe_reports

    def count_mostly_safe_reports(self):
        safe_reports = 0
        for report in self.reports:
            if is_report_mostly_safe(report):
                safe_reports += 1
        return safe_reports

    def part1(self):
        return self.count_safe_reports()

    def part2(self):
        return self.count_mostly_safe_reports()
