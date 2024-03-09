// Online C compiler to run C program online
#include <stdio.h>

int main() {
    double m, a, b;
    while (1) {
        scanf("%lf %lf %lf", &m, &a, &b);
        if (m == 0 && a == 0 && b == 0)
        break;
        
        int time = round(m * 3600 * (1 / a - 1 / b)) ;
        
        int hour = time / 3600;
        int minute = (time % 3600) / 60;
        int sec = time% 60;
        printf("%d:%02d:%02d\n", hour, minute, sec);
    }
    return 0;
}