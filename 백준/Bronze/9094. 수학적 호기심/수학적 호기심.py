import sys
input = sys.stdin.readline
x = int(input())
for i in range(x):
    count = 0
    n, m = map(int, input().split())
    for j in range(1, n):
        for k in range(j + 1, n):
            if ((j**2+k**2+m)%(j*k)) == 0:
                count += 1
                #print(j, k)
    print(count) 