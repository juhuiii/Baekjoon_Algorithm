#include <stdio.h>
int main(){
    int n, m, i, j;
    int arr[101] = {0};
    scanf("%d %d", &n, &m);
    for(int k = 1; k <= n; k++){
        arr[k] = k;
    }
    for(int k = 0; k < m; k++){
        scanf("%d %d", &i, &j);
        int temp = 0;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    for(int k = 1; k <= n; k++){
        printf("%d ", arr[k]);
    }
    return 0;
}