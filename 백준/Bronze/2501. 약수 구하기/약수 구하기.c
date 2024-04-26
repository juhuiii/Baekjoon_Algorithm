#include <stdio.h>
int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int cnt = 0;
    for(int i = 1; i <= n; i++){
        if(n % i == 0){
            cnt++;
            if(cnt == k){
                printf("%d", i);
                break;
            }
        }
    }
    if(cnt != k){
        printf("0");
    }
    return 0;
}