#include <stdio.h>
int main(){
  int a, b, c, t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++){
    scanf("%d %d %d", &a, &b, &c);
    if(a >= b + c || b >= a + c || c >= a + b){
      printf("Case #%d: invalid!\n", i);
    }
    else if(a == b && b == c){
      printf("Case #%d: equilateral\n", i);
    }
    else if(a == b || b == c){
      printf("Case #%d: isosceles\n", i);
    }
    else if(a != b && b != c){
      printf("Case #%d: scalene\n", i);
    }
  }
  return 0;
} 