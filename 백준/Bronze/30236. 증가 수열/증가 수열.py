N = int(input())
for _ in range(N):
    n = int(input())
    k = [i for i in range(1,n+1)]
    lst = list(map(int, input().split()))
    
    for i in range(len(k)):
        if k[i] == lst[i]:
            k[i] += 1
    
        for j in range(i+1, len(k)):
            if k[j-1] >= k[j]:
                k[j] += (k[j-1] - k[j]) + 1
                
    print(k[-1])