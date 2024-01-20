#include <stdio.h>
int main(){
  int n, milk ;
  scanf("%d", &n);

  int count = 0;
  int standard = 0;

  for (int i = 0; i < n; i++){
    scanf("%d", &milk);

    if (standard == 0 && milk == 0){
      count++;
      standard = 1;
    }
    else if (standard == 1 && milk == 1){
      count++;
      standard = 2;
    }
    else if (standard == 2 && milk == 2){
      count++;
      standard = 0;
    }
  }
  printf("%d\n", count);
}