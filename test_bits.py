from combinational_circuit import Bit, nand, compile_program, write_test
from single_bit_gates import mux, dmux
import unittest

class TestSingleBit(unittest.TestCase):

    def ex1(self):
        a = Bit()
        b = Bit()
        c = Bit()
        x = ~a & (b | c)
        y = nand(b, x)

        ex1inputs = """0 0 0\n0 0 1\n0 1 0\n0 1 1\n1 0 0\n1 0 1\n1 1 0\n1 1 1\n"""
        ex1outputs = """ 0 1\n 1 1\n 1 0\n 1 0\n 0 1\n 0 1\n 0 1\n 0 1\n"""
        write_test('ex1', ex1inputs, ex1outputs)

        compile_program([x, y])

    def ex2(self):
        a = Bit()
        b = Bit()
        inputs = "0 0\n0 1\n1 0\n1 1\n"
        outputs = " 0\n 0\n 0\n 1\n"
        write_test('ex2', inputs, outputs)
        compile_program([a & b])

    def ex3(self):
        a = Bit()
        b = Bit()
        c = Bit()
        x = (a & b) | (~c & nand(b, a))
        y = ~x
        inputs = "1 1 1\n1 1 0\n1 0 1\n1 0 0\n0 1 1\n0 1 0\n0 0 1\n0 0 0\n"
        outputs =  " 1 0\n 1 0\n 0 1\n 1 0\n 0 1\n 1 0\n 0 1\n 1 0\n"
        write_test('ex3', inputs, outputs)
        compile_program([x, y]) 

    def mux_test(self):
        a = Bit()
        b = Bit()
        s = Bit()
        inputs = "0 0 0\n0 0 1\n0 1 0\n0 1 1\n1 0 0\n1 0 1\n1 1 0\n1 1 1"
        outputs = " 0\n 0\n 0\n 1\n 1\n 0\n 1\n 1\n"
        write_test('mux', inputs, outputs)
        compile_program([a, b, s])

    def dmux_test(self):
        a = Bit()
        s = Bit()
        inputs = "0 0\n0 1\n1 0\n1 1\n"
        outputs = " 0 0\n 0 0\n 1 0\n 0 1\n"
        write_test('dmux', inputs, outputs)
        compile_program([a, s])


if __name__ == '__main__':
    unittest.main()


