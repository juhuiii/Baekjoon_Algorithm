#include <stdio.h>
#include <string.h> //string length

int main(){
  int n;
  scanf("%d\n", &n);
  char sen[101];

  for(int i = 1; i <= n; ++i){
    gets(sen);

    int len = strlen(sen);
    int count = 0, ind = 0;

    while (count < 2){
      if(sen[ind++] == ' ')
        count += 1;
    }
    for(int j = ind; j < len; ++j){
      printf("%c", sen[j]);
    }
    printf(" ");
    for(int j = 0; j < ind - 1; ++j) {
      printf("%c", sen[j]);
    }
    printf("\n");
  }
  return 0;
} 