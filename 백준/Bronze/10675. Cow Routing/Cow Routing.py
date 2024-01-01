a, b, n = map(int, input().split())
l2 = []
for i in range(n):
    x, y = map(int, input().split())
    l = list(map(int, input().split()))
    if l.count(a) > 0 and l.count(b) > 0:
        if l.index(b) > l.index(a):
            l2.append(x)
if l2 == []:
    print(-1)
else:
    print(min(l2))