#include <stdio.h>
int main(){
  int t, n, d;
  scanf("%d", &t);
  int v, f, c;
  for(int i = 0; i < t; i++){
    scanf("%d %d", &n, &d);
    int count = 0;
    for(int j = 0; j < n; j++){
      scanf("%d %d %d", &v, &f, &c);
      double result = (double)f / c;
      if(result * v >= d){
        count ++;
      }
    }
    printf("%d\n", count);
  }
  return 0;
}