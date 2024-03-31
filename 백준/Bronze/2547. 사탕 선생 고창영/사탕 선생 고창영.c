#include <stdio.h>
int main(){
  int t;
  scanf("%d", &t);
  for (int a =0 ; a<t; a++){
    long long int n;
    scanf("%lld", &n);
    long long int d, sum = 0;
    for(int i = 0; i < n; i++){
      scanf("%lld", &d);
      sum += d;
      sum = sum % n;
    }
    if (sum == 0){
      printf("YES\n");
    }
    else {
      printf("NO\n");
    }
  }
  return 0;
}