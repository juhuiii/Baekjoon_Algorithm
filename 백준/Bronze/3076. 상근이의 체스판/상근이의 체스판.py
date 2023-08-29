r, c = map(int, input().split())
a, b = map(int, input().split())
l = []
n = []
s = []
for i in range(c):
    if i % 2 == 0:
        for i in range(b):
            n.append("X")
        for i in range(b):
            s.append(".")
    else:
        for i in range(b):
            n.append(".")
        for i in range(b):
            s.append("X")
x = ''.join(n)
y = ''.join(s)
for i in range(r):
    for j in range(a):
        if i % 2 == 0:
            l.append(x)
        else:
            l.append(y)
for i in l:
    print(i)