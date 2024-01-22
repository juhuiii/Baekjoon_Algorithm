n = int(input())
for i in range(n):
    l = []
    a = int(input())
    for j in range(2, a + 1):
        while True:
            if a % j == 0:
                l.append(j)
                a = a // j
            else:
                break
    l.sort()
    l2 = set(l)
    k = sorted(list(l2))
    for i in range(len(k)):
        print(k[i], l.count(k[i])) 