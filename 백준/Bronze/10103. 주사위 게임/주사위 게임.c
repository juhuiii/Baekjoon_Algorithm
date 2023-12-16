#include <stdio.h>
int main()
{
    int a, b, n = 0;
    int s1 = 100, s2 = 100;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d %d", &a, &b);
        if(a > b){
            s2 = s2 - a;
        }
        else if(a < b){
            s1 = s1 - b;
        }
    }

    printf("%d\n", s1);
    printf("%d", s2);
    return 0;
}