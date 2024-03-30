#include <stdio.h>
int main(){
  int a = 0, b = 0, c = 0, t;
  scanf("%d", &t);
  while(t != 0){
    if(t >= 300){
      a += 1;
      t -= 300;
    }
    else if (t >= 60) {
      b += 1;
      t -= 60;
    }
    else if (t >= 10) {
      c += 1;
      t -= 10;
    }
    else {
      break;
    }
  }
  if (t != 0) {
    printf("-1");
  }
  else{
    printf("%d %d %d", a, b, c);
  }
}