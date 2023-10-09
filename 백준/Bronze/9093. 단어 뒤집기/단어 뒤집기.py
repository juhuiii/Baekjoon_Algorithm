a = int(input())
for i in range(a):
    b = list(input().split())
    for j in range(len(b)):
        print(b[j][::-1],end = ' ')