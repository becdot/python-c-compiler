"""
An example circuit to compile.
"""

from combinational_circuit import Bit, nand, compile_program

a = Bit()
b = Bit()
c = Bit()
x = ~a & (b | c)
y = nand(b, x)

compile_program([x, y])
#. #include <stdio.h>
#. 
#. static int v[3];
#. static int out[2];
#. 
#. int eval(void) {
#.   out[0] = (!((!((!(v[0] & v[0])) & (!((!(v[1] & v[1])) & (!(v[2] & v[2])))))) & (!((!(v[0] & v[0])) & (!((!(v[1] & v[1])) & (!(v[2] & v[2]))))))));
#.   out[1] = (!(v[1] & (!((!((!(v[0] & v[0])) & (!((!(v[1] & v[1])) & (!(v[2] & v[2])))))) & (!((!(v[0] & v[0])) & (!((!(v[1] & v[1])) & (!(v[2] & v[2]))))))))));
#. }
#. 
#. int main() {
#.   int i, j;
#.   for (;;) {
#.     for (i = 0; i < 3; i += 1)
#.         if (1 != scanf("%d", &v[i])) return 0;
#.     eval();
#.     for (j = 0; j < 2; j += 1)
#.         printf(" %d", out[j]);
#.     printf("\n");
#.   }
#. }
#. 
