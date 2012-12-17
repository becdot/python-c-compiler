# TODO operators return new instances or modify self?

from combinational_circuit import Bit, nand, compile_program

class Byte(object):

    def __init__(self, bits):
        self.bits = bits
    def __repr__(self):
        return str([repr(bit) for bit in self.bits])
    def __len__(self):
        return len(self.bits)
    def __iter__(self):
        for bit in self.bits:
            yield bit

    def __invert__(self):
        return [~bit for bit in self.bits]
    def __and__(self, other):
        return [(bit1 & bit2) for bit1, bit2 in zip(self, other)]


a = Bit()
b = Bit()
c = Bit()
d = Bit()

m1 = Byte([a, b, a, b])
m2 = Byte([d, b, a, c])

compile_program(m1 & m2)