#include <stdio.h>
#include <string.h>
int main(){
    char word[100];
    scanf("%s", word);
    int a = strlen(word);
    for(int i = 0; i < a / 2; i++){
        if(word[i] != word[a - i - 1]){
            printf("0");
            return 0;
        }
    }
    printf("1");
    return 0;
}