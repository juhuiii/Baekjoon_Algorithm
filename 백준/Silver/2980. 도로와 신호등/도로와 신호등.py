n, l = map(int, input().split())
total = l
a = 0
for i in range(n):
    d, r, g = map(int, input().split())
    if (d+a) % (r + g) < r:
        total += r - (d+a) % (r + g)
        a += r - (d+a) % (r + g)
print(total)