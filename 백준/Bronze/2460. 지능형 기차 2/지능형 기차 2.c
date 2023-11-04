#include <stdio.h>
int main()
{
    int st[11] = {0};
    int out, in, max= 0;
    for(int i = 1; i<11; i++){
        scanf("%d %d\n", &out, &in);
        st[i] = st[i-1];
        st[i] -= out;
        st[i] += in;
    }
    
    for(int i = 1; i<11; i++){
        if(max < st[i]){
            max = st[i];
        }
    }
    printf("%d", max);
}