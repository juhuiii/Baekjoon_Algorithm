#include <stdio.h>
int main() {
  int a, as = 0, bs = 0;
  scanf("%d\n", &a);
  char arr[a+1];
  for(int i = 0; i < a; i++){
    scanf("%c", &arr[i]);
    if(arr[i] =='A'){
      as += 1;
    }
    if(arr[i] == 'B'){
      bs += 1;
    }
  }
  if(as > bs){
    printf("A");
  }
  else if(bs > as){
    printf("B");
  }
  else if(as == bs){
    printf("Tie");
  }

  return 0;
  }