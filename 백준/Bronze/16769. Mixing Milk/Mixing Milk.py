a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
if b + d > c:
    b = b + d - c
    d = c
else:
    d = b + d
    b = 0

if d + f > e:
    d = d + f - e
    f = e
else:
    f = d + f
    d = 0

if f + b > a:
    f = f + b - a
    b = a
else:
    b = f + b
    f = 0

if b + d > c:
    b = b + d - c
    d = c
else:
    d = b + d
    b = 0

print(b)
print(d)
print(f)