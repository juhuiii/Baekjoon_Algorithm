import sys
input = sys.stdin.readline
a, b = map(int, input().split())
l = []
count = 0
for _ in range(a):
    n = int(input())
    l.append(n)
for i in range(len(l)):
    for j in range(i, len(l)):
        if i != j:
            if l[i]+l[j] <= b:
                count += 1
print(count) 