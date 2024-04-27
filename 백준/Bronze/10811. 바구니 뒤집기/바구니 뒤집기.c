#include <stdio.h>
int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int arr[n];
    for(int k = 0; k < n; k++){
        arr[k] = k + 1;
    }
    int i = 0, j = 0;
    for(int k = 0; k < m; k++){
        scanf("%d %d", &i, &j);
        for(int s = i - 1; s < j; s++){
            int temp = arr[s];
            arr[s] = arr[j - 1];
            arr[j - 1] = temp;
            j--;
        }
    }
    for(int k = 0; k < n; k++){
        printf("%d ", arr[k]);
    }
    return 0;
} 