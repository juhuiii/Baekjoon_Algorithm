#include <stdio.h>
int main(){
  int a1, b1, c1, d1;
  int a2, b2, c2, d2;
  int a3 = 0, b3 = 0, c3 = 0, d3 = 0;
  int t;
  
  scanf("%d", &t);
  for(int i = 0; i < t; i++){
    scanf("%d %d %d %d %d %d %d %d", &a1, &b1, &c1, &d1, &a2, &b2, &c2, &d2);
    a3 = a1 + a2;
    if (a3 < 1)
    {
      a3 = 1;
    }

    b3 = b1 + b2;
    if (b3 < 1)
    {
      b3 = 1;
    }
    
    c3 = c1 + c2;
    if (c3 < 0)
    {
      c3 = 0;
    }
    
    d3 = d1 + d2;
    printf("%d\n", a3 + 5 * b3 + 2 * c3 + 2 * d3);
  }
  return 0;
}