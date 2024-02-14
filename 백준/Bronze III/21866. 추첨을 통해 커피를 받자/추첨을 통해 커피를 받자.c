#include <stdio.h>
int main(){
    int score[9];
    int max[9] = {100, 100, 200, 200, 300, 300, 400, 400, 500}; 
    int total = 0;
    for(int i = 0; i < 9; i++){
        scanf("%d", &score[i]);
        if(score[i] > max[i]){
            printf("hacker");
            return 0;
        }
        total += score[i];
    }
    
    if(total < 100){
        printf("none");
    }
    else{
        printf("draw");
    }
}