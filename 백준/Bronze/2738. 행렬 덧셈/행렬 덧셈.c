#include <stdio.h>
int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    int arr[100][100];
    int arr2[100][100];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d ", &arr[i][j]);
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d ", &arr2[i][j]);
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            printf("%d ", arr[i][j] + arr2[i][j]);
            if(j==m-1)
              printf("\n");
        }
    }
    return 0;
} 