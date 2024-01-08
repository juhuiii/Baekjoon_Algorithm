n = int(input())
l = list(map(int, input().split()))
l2 = n * [1]
while True:
    if l.count(0) == n:
        print(*l2)
        break
    else:
        for i in range(n):
            if l[i] != 0:
                l[i] -= 1
                for j in range(n):
                    if l[j] != 0:
                        l2[j] += 1