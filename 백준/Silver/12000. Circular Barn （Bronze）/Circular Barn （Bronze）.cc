#include <bits/stdc++.h>
using namespace std;
 
int n, room[1001];
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
 
    cin >> n;
    for(int i = 1; i <= n; i++) cin >> room[i];
 
    int ans = 1e9;
    for(int i = 1; i <= n; i++) {
        int total = 0;
        for(int j = 1; j <= n; j++) {
            if(j >= i) total += (j - i) * room[j];
            else total += (j + n - i) * room[j];
        }
        ans = min(ans, total);
    }
 
    cout << ans << '\n';
    return 0;
}