#include <stdio.h>
#include <string.h>

int main(void){
    int a, repeat;
    char str[20];
    
    scanf("%d",&a);
    
    for(int i=0;i<a;i++){
        scanf("%d %s",&repeat,&str);
        int len = strlen(str);
        for(int j=0;j<len;j++){
            for(int n=0;n<repeat;n++)
               printf("%c",str[j]);
        }
        printf("\n");
    }
    return 0;
    
    
}