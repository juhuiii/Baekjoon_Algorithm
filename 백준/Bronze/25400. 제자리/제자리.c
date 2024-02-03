#include <stdio.h>
int main(){
  int n;
  int arr[250000];
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    scanf("%d", &arr[i]);
  }
  int num = 1;
  int count = 0;
  for (int i = 0; i < n; i++){
    if(num == arr[i]){
      num++;
      continue;
    }
  count ++;
  }
  printf("%d", count);
  return 0;
} 