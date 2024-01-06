#include <stdio.h>
int main(){
  int n, m, count = 0, temp;
  char k;
  scanf("%d %d", &n, &m);

  for(int i = 0; i < n; i++){
    temp = 0;
    for(int j = 0; j < m; j++){
      scanf(" %c", &k);
      if(k == 'O') temp ++;
    }
    if (temp > m / 2) count++;
  }
  printf("%d", count);
  return 0;
}