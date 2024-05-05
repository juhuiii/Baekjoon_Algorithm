#include <stdio.h>
int main(){
    int n, i, j, x, y, z = 0;
    scanf("%d", &n);

    for(i = 1; i < n; i++){
        x = i;
        y = i;
        for(j = 0; j < 8; j++){
            x += y % 10;
            y /= 10;
        }
        if(x == n){
            printf("%d", i);
            z = 1;
            break;
        }
    }
    if (z == 0)
        printf("0");
} 