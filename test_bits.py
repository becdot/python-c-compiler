from combinational_circuit import Bit, nand, compile_program, write_test
from single_bit_gates import mux as bit_mux, dmux as bit_dmux
import sys

"""Tests all single-bit functions (several examples, mux, dmux) by writing test files (input, expected output) and 
    compiling the individual c programs.  Tests can only be called one at a time.
   Useage: $ ./test_runner.sh 
            - loops over each of the tests
            - calls ./ex.sh <test_name> which calls test_bits.py <test_name>
            - test_bits checks test_name against the defined tests and 
                - writes tests (test-input, expected-output, test-output (blank))
                - prints out the C code for that test
            - ex.sh redirects stdo into test_name.c, compiles the c program, tests it with the provided inputs, 
              and runs a diff of the test-output and the expected-output
            - test_runner moves onto the next test and repeats until all tests have been checked"""

def ex1():
    a = Bit()
    b = Bit()
    c = Bit()
    x = ~a & (b | c)
    y = nand(b, x)

    test_values = """\
000 01
001 11
010 10
011 10
100 01
101 01
110 01
111 01"""
    inputs = '\n'.join(' '.join(line.split(' ')[0]) for line in test_values.splitlines())
    outputs = ''.join(' ' + out + '\n' for out in (' '.join(line.split(' ')[1]) for line in test_values.splitlines()))
    write_test('ex1', inputs, outputs)
    compile_program([x, y])

def ex2():
    a = Bit()
    b = Bit()
    test_values = """\
00 0
01 0
10 0
11 1"""
    inputs = '\n'.join(' '.join(line.split(' ')[0]) for line in test_values.splitlines())
    outputs = ''.join(' ' + out + '\n' for out in (' '.join(line.split(' ')[1]) for line in test_values.splitlines()))
    write_test('ex2', inputs, outputs)
    compile_program([a & b])

def ex3():
    a = Bit()
    b = Bit()
    c = Bit()
    x = (a & b) | (~c & nand(b, a))
    y = ~x
    test_values = """\
111 10
110 10
101 01
100 10
011 01
010 10
001 01
000 10"""
    inputs = '\n'.join(' '.join(line.split(' ')[0]) for line in test_values.splitlines())
    outputs = ''.join(' ' + out + '\n' for out in (' '.join(line.split(' ')[1]) for line in test_values.splitlines()))
    write_test('ex3', inputs, outputs)
    compile_program([x, y]) 

def ex4():
    a = Bit()
    b = Bit()
    x = (a & b) ^ (~a)
    y = a ^ x
    test_values = """\
00 11
01 11
10 01
11 10"""
    inputs = '\n'.join(' '.join(line.split(' ')[0]) for line in test_values.splitlines())
    outputs = ''.join(' ' + out + '\n' for out in (' '.join(line.split(' ')[1]) for line in test_values.splitlines()))
    write_test('ex4', inputs, outputs)
    compile_program([x, y])

def mux():
    a = Bit()
    b = Bit()
    s = Bit()
    test_values = """\
000 0
001 0
010 0
011 1
100 1
101 0
110 1
111 1"""
    inputs = '\n'.join(' '.join(line.split(' ')[0]) for line in test_values.splitlines())
    outputs = ''.join(' ' + out + '\n' for out in (' '.join(line.split(' ')[1]) for line in test_values.splitlines()))
    write_test('mux', inputs, outputs)
    bit_mux(a, b, s)

def dmux():
    a = Bit()
    s = Bit()
    test_values = """\
00 00
01 00
10 10
11 01"""
    inputs = '\n'.join(' '.join(line.split(' ')[0]) for line in test_values.splitlines())
    outputs = ''.join(' ' + out + '\n' for out in (' '.join(line.split(' ')[1]) for line in test_values.splitlines()))
    write_test('dmux', inputs, outputs)
    bit_dmux(a, s)

test_dict = {'ex1': ex1, 'ex2': ex2, 'ex3': ex3, 'ex4': ex4, 'mux': mux, 'dmux': dmux}
test_dict[sys.argv[1]]()
