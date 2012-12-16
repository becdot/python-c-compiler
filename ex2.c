#include <stdio.h>

static int v[2];
static int out[1];

int eval(void) {
int x0 = !(v[0] & v[1]);
int x1 = !(x0 & x0);
out[0] = x1;
}

int main() {
  int i, j;
  for (;;) {
    for (i = 0; i < 2; i += 1)
        if (1 != scanf("%d", &v[i])) return 0;
    eval();
    for (j = 0; j < 1; j += 1)
        printf(" %d", out[j]);
    printf("\n");
  }
}
