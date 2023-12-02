#include <stdio.h>
int main(){
  int n, arr[50];
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
    scanf("%d", &arr[i]);
    if(arr[1] - arr[0] == arr[2] - arr[1])
      printf("%d", arr[n - 1] + (arr[1] - arr[0]));
    else
      printf("%d", arr[n - 1] * (arr[1] / arr[0]));
} 