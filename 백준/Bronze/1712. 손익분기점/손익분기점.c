#include <stdio.h>
int main(){
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  if (b >= c)
  {
    printf("-1");
    return 0;
  }
  int res = a / (c - b) + 1;
  printf("%d", res);
}