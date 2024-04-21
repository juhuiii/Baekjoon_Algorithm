#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);
    int a = 0;
    int q, d, n, p = 0;
    for(int i = 0; i < t; i++){
        scanf("%d", &a);
        q = a / 25;
        a -= q * 25;
        d = a / 10;
        a -= d * 10;
        n = a / 5;
        a -= n * 5;
        p = a;
        printf("%d %d %d %d\n", q, d, n, p);
    }
    return 0;
}