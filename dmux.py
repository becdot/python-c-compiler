from combinational_circuit import Bit, nand, compile_program

a = Bit()
sel = Bit()

dmux_a, dmux_b = (a & ~sel), (a & sel)
compile_program([dmux_a, dmux_b])