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
    test_values = """\
0000 0000
0001 0000
0010 0000
0011 0000
0100 0100
0101 0100
0110 0101
0111 0101
1000 0010
1001 1010
1010 0010
1011 1010
1100 0110
1101 1110
1110 0111
1111 1111"""
    inputs = '\n'.join(' '.join(line.split(' ')[0]) for line in test_values.splitlines())
    outputs = ''.join(' ' + out + '\n' for out in (' '.join(line.split(' ')[1]) for line in test_values.splitlines()))
    write_test("byte_and", inputs, outputs)
    compile_program(m1 & m2)



test_dict = {'byte_and': byte_and}
test_dict[sys.argv[1]]()