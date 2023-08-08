a, b, c, d = map(int, input().split())
l = []
l2 = []
l3 = []
for i in range(a):
    s = str(input())
    l.append(s)
for i in l:
    example = []
    for j in i:
        example.append(j*d)
    l2.append("".join(example))
for i in l2:
    for j in range(c):
        l3.append(i)
for i in l3:
    print(i)