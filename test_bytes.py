from combinational_circuit import Bit, compile_program, write_test
from byte import Byte
import sys

def byte_and():
    a = Bit()
    b = Bit()
    c = Bit()
    d = Bit()

    m1 = Byte([a, b, a, b])
    m2 = Byte([d, b, a, c])
    inputs = "0 0 0 0\n0 0 0 1\n0 0 1 0\n0 0 1 1\n0 1 0 0\n0 1 0 1\n0 1 1 0\n0 1 1 1\n1 0 0 0\n\
1 0 0 1\n1 0 1 0\n1 0 1 1\n1 1 0 0\n1 1 0 1\n1 1 1 0\n1 1 1 1"
    outputs = " 0 0 0 0\n 0 0 0 0\n 0 0 0 0\n 0 0 0 0\n 0 1 0 0\n 0 1 0 0\n 0 1 0 1\n 0 1 0 1\n\
 0 0 1 0\n 1 0 1 0\n 0 0 1 0\n 1 0 1 0\n 0 1 1 0\n 1 1 1 0\n 0 1 1 1\n 1 1 1 1\n"
    write_test("byte_and", inputs, outputs)
    compile_program(m1 & m2)



test_dict = {'byte_and': byte_and}
test_dict[sys.argv[1]]()