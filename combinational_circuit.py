"""
Really basic compiler from combinational circuits to C.
"""
import itertools

inputs = []                     # All input bits
intermediates = []
count = itertools.count()

class Bit(object):
    """A signal in the circuit -- either an input bit or the output of
    a gate."""
    def __init__(self, expr=None):
        if expr is None:
            self.expr = 'v[%d]' % len(inputs)
            inputs.append(self)
        else:
            self.expr = expr
    def __repr__(self):
        return self.expr
    def __invert__(self):
        return nand(self, self)
    def __and__(self, other):
        return ~nand(self, other)
    def __or__(self, other):
        # a|b = ~(~a & ~b) = ~(~(~a nand ~b)) = ~a nand ~b
        return nand(~self, ~other)
    def __xor__(self, other):
        return nand((~(self & ~other)), (~(other & ~self)))

def nand(x, y):
    c = count.next()
    expr = '  int x%d = !(%s & %s);' % (c, x, y)
    intermediates.append(expr)
    return Bit('x%d' % (c))

def compile_program(output_bits):
    """Print out a C program whose action is to repeatedly:
    * read in values for all the input bits
    * compute the values of the output bits from the inputs
    * write out the output bits
    """
    print '#include <stdio.h>'
    print
    print 'static int v[%d];' % len(inputs)
    print 'static int out[%d];' % len(output_bits)
    print
    print 'int eval(void) {'
    for intermediate in intermediates:
        print intermediate
    for i, bit in enumerate(output_bits):
        print '  out[%d] = %s;' % (i, bit)
    print '}'
    print 
    print 'int main() {'
    print '  int i, j;'
    print '  for (;;) {'
    print '    for (i = 0; i < %d; i += 1)' % len(inputs)
    print '        if (1 != scanf("%d", &v[i])) return 0;'
    print '    eval();'
    print '    for (j = 0; j < %d; j += 1)' % len(output_bits)
    print '        printf(" %d", out[j]);'
    print '    printf("\\n");'
    print '  }'
    print '}'

def write_test(testname, inputs, outputs):
    with open('{}.test-input'.format(testname), 'w') as infile, open('{}.expected-output'.format(testname), 'w') as expectfile, \
         open('{}.test-output'.format(testname), 'w') as outfile:
        infile.write(inputs)
        expectfile.write(outputs)
        outfile.write('')
    infile.close()
    expectfile.close()
    outfile.close()
