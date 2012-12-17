from combinational_circuit import Bit, nand, compile_program

a = Bit()
b = Bit()
sel = Bit()

mux = (a & ~sel) | (b & sel)
compile_program([mux])

