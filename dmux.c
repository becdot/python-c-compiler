#include <stdio.h>

static int v[2];
static int out[2];

int eval(void) {
  int x0 = !(v[1] & v[1]);
  int x1 = !(v[0] & x0);
  int x2 = !(x1 & x1);
  int x3 = !(v[0] & v[1]);
  int x4 = !(x3 & x3);
  out[0] = x2;
  out[1] = x4;
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
