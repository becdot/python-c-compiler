"""
An example circuit to compile.
"""

from combinational_circuit import Bit, nand, compile_program

a = Bit()
b = Bit()
x = a & b

compile_program([x])