#include <stdio.h>
int main(){
  int n, k, p, result = 0;
  scanf("%d %d %d", &n, &k, &p);
  for (int i = 0; i < n; i++){
    int cream = 0;
    for(int j = 0; j < k; j++){
      int index;
      scanf("%d", &index);
      cream += index;
    }

    if (k - cream < p){
      result += 1;
    }
  }
  printf("%d", result);
  
} 