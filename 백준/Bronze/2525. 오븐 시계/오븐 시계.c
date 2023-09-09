#include <stdio.h>
int main()
{
    int a, b, c;
    scanf("%d %d\n", &a, &b);//a가 시, b가 분
    scanf("%d", &c);//c는 조리 시간
    int sum = a*60+b+c;
    if(sum>=1440){
        sum  = sum -1440;
        printf("%d %d",sum/60, sum%60);
    }
    else{
        printf("%d %d",sum/60, sum%60);
    }
    return 0;
}