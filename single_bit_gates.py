from combinational_circuit import compile_program, write_test
"""Logic gates for a single-bit -- prints out a C program using compile_program"""

def dmux(bit, sel):
    dmux_a, dmux_b = (bit & ~sel), (bit & sel)
    compile_program([dmux_a, dmux_b])

def mux(bit1, bit2, sel):
    bit = (bit1 & ~sel) | (bit2 & sel)
    compile_program([bit])