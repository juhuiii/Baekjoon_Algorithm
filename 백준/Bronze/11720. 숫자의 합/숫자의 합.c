#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    char s[100] = {0};
    scanf("%s", &s);
  
    int sum = 0;
    for(int i = 0; i < n; i++){
        sum = sum + s[i] - '0';
    }
    printf("%d", sum);
} 