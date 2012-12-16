"""
An example circuit to compile.
"""

from combinational_circuit import Bit, nand, compile_program

a = Bit()
b = Bit()
c = Bit()
x = (a & b) | (~c & nand(b, a))
y = ~x

compile_program([x, y])