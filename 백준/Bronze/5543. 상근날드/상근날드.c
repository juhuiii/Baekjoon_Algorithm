#include <stdio.h>
int main()
{
	int a, b, min1 = 2000, min2 = 2000 ;
  for(int i = 0; i < 3; i++){
    scanf("%d", &a);
    if( min1 > a)
      min1 = a;
  }
  for (int j = 0 ; j < 2; j++){
    scanf("%d", &b);
    if (min2 > b)
      min2 = b;
  }
  printf("%d", min1 + min2 - 50);
}