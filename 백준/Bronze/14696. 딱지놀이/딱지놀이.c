#include <stdio.h>

int main() {
	int a[5], b[5];
	int i, j, k, n, m;
	char x;
	scanf("%d", &n);
	for(i = 1; i <= n; i++){
		for(j = 1; j <= 4; j++) a[j] = 0;
		scanf("%d", &k);
		for(j = 1; j <= k; j++){
			scanf("%d", &m);
			a[m]++;
		}
		
		for(j = 1; j <= 4; j++) b[j] = 0;
		scanf("%d", &k);
		for(j = 1; j <= k; j++){
			scanf("%d", &m);
			b[m]++;
		}
		x = 0;
		for(j = 4; j >= 1; j--){
			if(b[j] < a[j])
            {
				x = 'A';
				break;
			}
			if(a[j] < b[j])
            {
				x = 'B';
				break;
			}
		}
		if(x == 0) x = 'D';
		printf("%c\n", x);
	}
	return 0;
}