#include <stdio.h>
int main(){
  char str [100] ;
  scanf("%s", &str);
  int in;
  for(int i = 97; i < 123; i++){
    in = -1;
    for(int j = 0; j < strlen(str); j++){
      if (i == (int)str[j]){
        in = j;
        break;
      }
    }
    printf("%d ", in);
  }
  
  return 0;
} 