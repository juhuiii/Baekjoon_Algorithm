#include <stdio.h>
int main(){
    int s1, s2, s3;
    scanf("%d %d %d", &s1, &s2, &s3);
    int n, a, b, c, count = 0, max = 0;
    scanf("%d", &n);
    int total = 0;
    for(int i = 0; i < 3*n; i++){
        scanf("%d %d %d", &a, &b, &c);
        count++;
        if(count <= 3){
            total += a*s1 + b*s2 + c*s3;
            if(total > max){
                max = total;
                }
            if(count == 3){
                total = 0; 
                count = 0;
            }
            }
        }
    printf("%d", max);
    return 0;
} 