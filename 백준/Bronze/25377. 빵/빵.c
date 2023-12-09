#include <stdio.h>
int main(){
  int n, result = -1;
  scanf("%d", &n);
  for(int i = 0; i < n; i++)
    {
      int a, b;
      scanf("%d %d", &a, &b);
      if(a <= b && (result == -1 || result > b))
        result = b;
    }
  printf("%d", result);
} 