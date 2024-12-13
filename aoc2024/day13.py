from aoc2024.day import Day


# Oh, this is fun, isn't it?
#
# 94a + 22b = 8400
# 34a + 67b = 5400
# a = (8400 - 22b) / 94
# a = (5400 - 67b) / 34
#
# (8400 - 22b) / 94 = (5400 - 67b) / 34
# 34 (8400 - 22b) = 94 (5400 - 67b)
# 34×8400 - 34×22b = 94×5400 - 94×67b
# 94×67b - 34×22b = 94×5400 - 34×8400
# b(94×67 - 34×22) = 94×5400 - 34×8400
# b = 94×5400 - 34×8400 / 94×67 - 34×22
#
#                               (button A X movement × Y result) - (button A Y movement × X result)
# Button B presses = -----------------------------------------------------------------------------------------
#                    (button A X movement × button B Y movement) - (button A Y movement × button B X movement)
def find_solution(machine):
    button_a_x_movement_times_y_result = machine.a[0] * machine.p[1]
    button_a_y_movement_times_x_result = machine.a[1] * machine.p[0]
    button_a_x_movement_times_button_b_y_movement = machine.a[0] * machine.b[1]
    button_a_y_movement_times_button_b_x_movement = machine.a[1] * machine.b[0]
    b_moves = ((button_a_x_movement_times_y_result - button_a_y_movement_times_x_result)
               / (button_a_x_movement_times_button_b_y_movement - button_a_y_movement_times_button_b_x_movement))
    a_moves = (machine.p[0] - b_moves * machine.b[0]) / machine.a[0]
    if a_moves != int(a_moves) or b_moves != int(b_moves):
        return None
    return a_moves, b_moves, int(a_moves * 3 + b_moves)


def find_best_token_cost(machines):
    return sum([solution[2] for solution in [find_solution(machine) for machine in machines] if solution is not None])


class Machine:
    def __init__(self, input_record=None, a=None, b=None, p=None):
        if input_record is None:
            self.a = a
            self.b = b
            self.p = p
        else:
            self.a = (input_record["Button A"]["X"], input_record["Button A"]["Y"])
            self.b = (input_record["Button B"]["X"], input_record["Button B"]["Y"])
            self.p = (input_record["Prize"]["X"], input_record["Prize"]["Y"])

    def __repr__(self):
        return f"a = {self.a}, b = {self.b}, p = {self.p}"

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.p == other.p


class Day13(Day):
    machines = None

    def load(self, input_file):
        self.machines = []
        with open(input_file, 'r') as file:
            input_record = {}
            while line := file.readline():
                fields = [value.strip() for value in line.split(":")]
                if len(fields) < 2:
                    self.machines.append(Machine(input_record))
                    input_record = {}
                else:
                    input_record[fields[0]] = {}
                    for value in [value.strip() for value in fields[1].split(",")]:
                        input_record[fields[0]][value[0]] = int(value[2:])
            if input_record is not None:
                self.machines.append(Machine(input_record))

    def part1(self):
        return find_best_token_cost(self.machines)

    def part2(self):
        rigged_machine_offset = 10000000000000
        rigged_machines = [
            Machine(
                a=machine.a,
                b=machine.b,
                p=(machine.p[0] + rigged_machine_offset, machine.p[1] + rigged_machine_offset))
            for machine in self.machines]
        return find_best_token_cost(rigged_machines)
