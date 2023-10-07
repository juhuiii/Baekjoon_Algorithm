#include <stdio.h>
int main(){
    int n, v = 0;
    int a[100];
    scanf("%d", &n);
    for(int i = 0; i<n; i++){
        scanf("%d ", &a[i]);
    }
    scanf("%d", &v);
    int count = 0;
    for(int i = 0; i<n; i++){
        if(v==a[i]){
            count++;

        }
    }
    printf("%d", count);
    return 0;
}