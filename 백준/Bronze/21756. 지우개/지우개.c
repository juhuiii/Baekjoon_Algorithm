#include <stdio.h>
int main(){
  int a[100], b [100];

  int n;
  scanf("%d", &n);
  for(int i = 0 ; i < n; i++){
    a[i] = i + 1;
  }

  while(n > 1){
    int j = 0;
    for(int i = 0; i < n; i++){
      if (i % 2 == 1){
        b[j] = a[i];
        j++;
      }
    }
    for(int i = 0; i < n; i++){
      a[i] = b[i];
    }
    n = j;
  }
  printf("%d\n", a[0]);
}