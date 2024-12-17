import unittest

from ..day17 import Day17, Computer


class TestDay17(unittest.TestCase):
    def setUp(self):
        self.day17 = Day17()

    def test_load(self):
        self.day17.load("inputs/day17/test_input.txt")
        expected = Computer(a=729, program=[0, 1, 5, 4, 3, 0])
        self.assertEqual(expected, self.day17.computer)

    def test_combo_operand_value(self):
        computer = Computer(a=5, b=676, c=14)
        self.assertEqual(0, computer.combo_operand_value(0))
        self.assertEqual(1, computer.combo_operand_value(1))
        self.assertEqual(2, computer.combo_operand_value(2))
        self.assertEqual(3, computer.combo_operand_value(3))
        self.assertEqual(5, computer.combo_operand_value(4))
        self.assertEqual(676, computer.combo_operand_value(5))
        self.assertEqual(14, computer.combo_operand_value(6))

    def test_adv_3(self):
        computer = Computer(a=8)
        computer.adv(3)
        self.assertEqual(1, computer.a)

    def test_adv_b(self):
        computer = Computer(a=8, b=2)
        computer.adv(5)
        self.assertEqual(2, computer.a)

    def test_bxl(self):
        computer = Computer(b=5)
        computer.bxl(7)
        self.assertEqual(2, computer.b)

    def test_bst(self):
        computer = Computer(b=5, c=9)
        computer.bst(6)
        self.assertEqual(1, computer.b)

    def test_jnz_zero(self):
        computer = Computer(ip=6)
        computer.jnz(4)
        self.assertEqual(8, computer.ip)

    def test_jnz_not_zero(self):
        computer = Computer(a=1, ip=6)
        computer.jnz(4)
        self.assertEqual(4, computer.ip)

    def test_bxc(self):
        computer = Computer(b=5, c=3)
        computer.bxc(7)
        self.assertEqual(6, computer.b)

    def test_out(self):
        computer = Computer(a=13)
        computer.out(4)
        self.assertEqual(5, computer.output[0])

    def test_bdv_c(self):
        computer = Computer(a=8, c=1)
        computer.bdv(6)
        self.assertEqual(4, computer.b)

    def test_cdv_0(self):
        computer = Computer(a=8)
        computer.cdv(0)
        self.assertEqual(8, computer.c)

    def test_run(self):
        computer = Computer(a=729, program=[0, 1, 5, 4, 3, 0])
        expected = [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]
        self.assertEqual(expected, computer.run())

    def test_find_register_a_value_to_produce_program_copy(self):
        computer = Computer(a=2024, program=[0, 3, 5, 4, 3, 0])
        expected = 117440
        self.assertEqual(expected, computer.find_register_a_value_to_produce_program_copy())
