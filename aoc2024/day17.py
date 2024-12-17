from aoc2024.day import Day


class Computer:
    def __init__(self, a=0, b=0, c=0, ip=0, program=None):
        self.a = a
        self.b = b
        self.c = c
        self.ip = ip
        self.program = [] if program is None else program[:]
        self.opcodes = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
        self.output = []

    def run(self):
        """
        A number called the instruction pointer identifies the position in the program from which the next opcode will
        be read; it starts at 0, pointing at the first 3-bit number in the program. Except for jump instructions, the
        instruction pointer increases by 2 after each instruction is processed (to move past the instruction's opcode
        and its operand). If the computer tries to read an opcode past the end of the program, it instead halts.

        :return: the program's output
        """
        while 0 <= self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            self.opcodes[opcode](operand)
        return self.output

    def adv(self, combo_operand):
        """
        The **adv** instruction (opcode **0**) performs **division**. The numerator is the value in the `A` register.
        The denominator is found by raising 2 to the power of the instruction's **combo** operand. (So, an operand of 2
        would divide `A` by `4 (2^2)`; an operand of `5` would divide `A` by `2^B`.) The result of the division
        operation is truncated to an integer and then written to the `A` register.

        :param combo_operand: the **combo** operand
        :return: None
        """
        denominator = 2 ** self.combo_operand_value(combo_operand)
        self.a = self.a // denominator
        self.ip += 2

    def bxl(self, literal_operand):
        """
        The **bxl** instruction (opcode **1**) calculates the **bitwise XOR** of register `B` and the instruction's
        **literal** operand, then stores the result in register `B`.

        :param literal_operand: the **literal** operand
        :return: None
        """
        self.b ^= literal_operand
        self.ip += 2

    def bst(self, combo_operand):
        """
        The **bst** instruction (opcode **2**) calculates the value of its **combo** operand modulo 8 (thereby keeping
        only its lowest 3 bits), then writes that value to the `B` register.

        :param combo_operand: the **combo** operand
        :return: None
        """
        self.b = self.combo_operand_value(combo_operand) % 8
        self.ip += 2

    def jnz(self, literal_operand):
        """
        The **jnz** instruction (opcode **3**) does nothing if the `A` register is `0`. However, if the `A` register is
        **not zero**, it **jumps** by setting the instruction pointer to the value of its **literal** operand; if this
        instruction jumps, the instruction pointer is **not** increased by 2 after this instruction.

        :param literal_operand: the **literal** operand
        :return: None
        """
        if self.a == 0:
            self.ip += 2
        else:
            self.ip = literal_operand

    def bxc(self, _operand):
        """
        The **bxc** instruction (opcode **4**) calculates the **bitwise XOR** of register `B` and register `C`, then
        stores the result in register `B`. (For legacy reasons, this instruction reads an operand but **ignores** it.)

        :param _operand: not used
        :return: None
        """
        self.b ^= self.c
        self.ip += 2

    def out(self, combo_operand):
        """
        The **out** instruction (opcode **5**) calculates the value of its **combo** operand modulo 8, then **outputs**
        that value. (If a program outputs multiple values, they are separated by commas.)

        :param combo_operand: the **combo** operand
        :return: None
        """
        value = self.combo_operand_value(combo_operand) % 8
        self.output.append(value)
        self.ip += 2

    def bdv(self, combo_operand):
        """
        The **bdv** instruction (opcode **6**) works exactly like the `adv` instruction except that the result is stored
        in the **B register**. (The numerator is still read from the `A` register.)

        :param combo_operand: the **combo** operand
        :return: None
        """
        denominator = 2 ** self.combo_operand_value(combo_operand)
        self.b = self.a // denominator
        self.ip += 2

    def cdv(self, combo_operand):
        """
        The **cdv** instruction (opcode **7**) works exactly like the `adv` instruction except that the result is stored
        in the **C register**. (The numerator is still read from the `A` register.)

        :param combo_operand: the **combo** operand
        :return: None
        """
        denominator = 2 ** self.combo_operand_value(combo_operand)
        self.c = self.a // denominator
        self.ip += 2

    def combo_operand_value(self, combo_operand) -> int:
        """
        The value of a **combo operand** can be found as follows:

        - Combo operands `0` through `3` represent literal values `0` through `3`.
        - Combo operand `4` represents the value of register `A`.
        - Combo operand `5` represents the value of register `B`.
        - Combo operand `6` represents the value of register `C`.
        - Combo operand `7` is reserved and will not appear in valid programs.

        :param combo_operand: the **combo** operand
        :return: the value of the **combo** operand
        """
        if combo_operand < 4:
            return combo_operand
        if combo_operand == 4:
            return self.a
        if combo_operand == 5:
            return self.b
        if combo_operand == 6:
            return self.c
        if combo_operand == 7:
            raise Exception("Illegal operation")

    def reset(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.ip = 0
        self.output = []

    def find_register_a_value_to_produce_program_copy(self, index=0, a=0):
        size = len(self.program)
        if index == size:
            return a
        for test_value in range(8):
            if index == 0 and test_value == 0:
                continue
            self.reset()
            self.a = a * 8 + test_value
            expected_output = self.program[size - index - 1:]
            output = self.run()
            if output == expected_output:
                found = self.find_register_a_value_to_produce_program_copy(index + 1, a * 8 + test_value)
                if found is not None:
                    return found

    def __repr__(self):
        return f"a={self.a}, b={self.b}, c={self.c}, ip={self.ip}, program={self.program}, output={self.output}"

    def __eq__(self, other):
        return (self.a == other.a and self.b == other.b and self.c == other.c and self.ip == other.ip
                and self.program == other.program and self.output == other.output)


class Day17(Day):
    computer = None

    def load(self, input_file):
        self.computer = None
        registers = {}
        program = []
        with open(input_file) as f:
            while line := f.readline():
                elements = [element.strip() for element in line.split(':')]
                if len(elements) == 2:
                    if elements[0].startswith("Register "):
                        registers[elements[0][-1]] = int(elements[1])
                    if elements[0] == "Program":
                        program = [int(a) for a in elements[1].split(',')]
            self.computer = Computer(a=registers["A"], b=registers["B"], c=registers["C"], program=program)

    def part1(self):
        return self.computer.run()

    def part2(self):
        return self.computer.find_register_a_value_to_produce_program_copy()
