a, b = map(int, input().split())
c = 0
l = []
for i in range(b):
    c += a
    c = str(c)
    d = 0
    for i in range(len(c)):
        d = d * 10 + int(c[len(c)-i-1])
    c = int(c)
    l.append(d)
print(max(l))