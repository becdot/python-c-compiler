#include <stdio.h>

static int v[2];
static int out[2];

int eval(void) {
  int x0 = !(v[0] & v[1]);
  int x1 = !(x0 & x0);
  int x2 = !(v[0] & v[0]);
  int x3 = !(x2 & x2);
  int x4 = !(x1 & x3);
  int x5 = !(x4 & x4);
  int x6 = !(x5 & x5);
  int x7 = !(x1 & x1);
  int x8 = !(x2 & x7);
  int x9 = !(x8 & x8);
  int x10 = !(x9 & x9);
  int x11 = !(x6 & x10);
  int x12 = !(x11 & x11);
  int x13 = !(v[0] & x12);
  int x14 = !(x13 & x13);
  int x15 = !(x14 & x14);
  int x16 = !(v[0] & v[0]);
  int x17 = !(x11 & x16);
  int x18 = !(x17 & x17);
  int x19 = !(x18 & x18);
  int x20 = !(x15 & x19);
  out[0] = x11;
  out[1] = x20;
}

int main() {
  int i, j;
  for (;;) {
    for (i = 0; i < 2; i += 1)
        if (1 != scanf("%d", &v[i])) return 0;
    eval();
    for (j = 0; j < 2; j += 1)
        printf(" %d", out[j]);
    printf("\n");
  }
}
