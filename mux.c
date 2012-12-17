#include <stdio.h>

static int v[3];
static int out[1];

int eval(void) {
  int x0 = !(v[2] & v[2]);
  int x1 = !(v[0] & x0);
  int x2 = !(x1 & x1);
  int x3 = !(v[1] & v[2]);
  int x4 = !(x3 & x3);
  int x5 = !(x2 & x2);
  int x6 = !(x4 & x4);
  int x7 = !(x5 & x6);
  out[0] = x7;
}

int main() {
  int i, j;
  for (;;) {
    for (i = 0; i < 3; i += 1)
        if (1 != scanf("%d", &v[i])) return 0;
    eval();
    for (j = 0; j < 1; j += 1)
        printf(" %d", out[j]);
    printf("\n");
  }
}
