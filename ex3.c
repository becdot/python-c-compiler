#include <stdio.h>

static int v[3];
static int out[2];

int eval(void) {
  int x0 = !(v[0] & v[1]);
  int x1 = !(x0 & x0);
  int x2 = !(v[2] & v[2]);
  int x3 = !(v[1] & v[0]);
  int x4 = !(x2 & x3);
  int x5 = !(x4 & x4);
  int x6 = !(x1 & x1);
  int x7 = !(x5 & x5);
  int x8 = !(x6 & x7);
  int x9 = !(x8 & x8);
  out[0] = x8;
  out[1] = x9;
}

int main() {
  int i, j;
  for (;;) {
    for (i = 0; i < 3; i += 1)
        if (1 != scanf("%d", &v[i])) return 0;
    eval();
    for (j = 0; j < 2; j += 1)
        printf(" %d", out[j]);
    printf("\n");
  }
}
