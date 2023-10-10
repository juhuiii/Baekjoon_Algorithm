n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    total = 0
    l = []
    num = 0
    for j in range(b):
        c, d = map(int, input().split())
        l.append(c*d)
    while True:
        if total >= a:
            print(num)
            break
        total += max(l)
        num += 1
        l.remove(max(l)) 