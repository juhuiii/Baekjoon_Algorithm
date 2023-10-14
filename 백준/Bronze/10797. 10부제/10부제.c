#include <stdio.h>
int main()
{
    int a;
    scanf("%d\n", &a);
    int c1, c2, c3, c4, c5;
    scanf("%d %d %d %d %d", &c1, &c2, &c3, &c4, &c5);
    int c[5] = {c1, c2, c3, c4, c5};
    int sum = 0;
    
    for(int i = 0; i<5; i++){
        if(a == c[i]){
            sum++;
            continue;
        }
        else{
            continue;
        }
    }
    printf("%d", sum);
    return 0;
}