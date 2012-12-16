#include <stdio.h>

static int v[3];
static int out[2];

int eval(void) {
int x0 = !(v[0] & v[0]);
int x1 = !(v[1] & v[1]);
int x2 = !(v[2] & v[2]);
int x3 = !(x1 & x2);
int x4 = !(x0 & x3);
int x5 = !(x4 & x4);
int x6 = !(v[1] & x5);
out[0] = x5;
out[1] = x6;
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
