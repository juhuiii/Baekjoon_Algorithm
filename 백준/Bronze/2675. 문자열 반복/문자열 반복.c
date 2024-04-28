#include <stdio.h>
#include <string.h>
int main() {
  int t, r;
  char s[20];

  scanf("%d", &t);

  for (int i = 0; i < t; i++){
    scanf("%d %s", &r, &s);
    int len = strlen(s);
    for (int j = 0; j < len; j++){
      for (int n = 0; n < r; n++)
        printf("%c", s[j]);
    }
    printf("\n");
  }
  return 0;
}