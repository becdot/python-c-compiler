#include <stdio.h>

static int v[4];
static int out[4];

int eval(void) {
  int x0 = !(v[0] & v[3]);
  int x1 = !(x0 & x0);
  int x2 = !(v[1] & v[1]);
  int x3 = !(x2 & x2);
  int x4 = !(v[0] & v[0]);
  int x5 = !(x4 & x4);
  int x6 = !(v[1] & v[2]);
  int x7 = !(x6 & x6);
  out[0] = x1;
  out[1] = x3;
  out[2] = x5;
  out[3] = x7;
}

int main() {
  int i, j;
  for (;;) {
    for (i = 0; i < 4; i += 1)
        if (1 != scanf("%d", &v[i])) return 0;
    eval();
    for (j = 0; j < 4; j += 1)
        printf(" %d", out[j]);
    printf("\n");
  }
}
