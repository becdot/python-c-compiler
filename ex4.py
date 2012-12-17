"""
An example circuit to compile.
"""

from combinational_circuit import Bit, nand, compile_program

a = Bit()
b = Bit()
x = (a & b) ^ (~a)
y = a ^ x

compile_program([x, y])

"""
a  b  x  y
0  0  1  1
0  1  1  1
1  0  0  1
1  1  1  0
"""