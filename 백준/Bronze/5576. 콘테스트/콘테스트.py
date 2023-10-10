a = []
b = []
for i in range(10) :
    a.append(int(input()))
for i in range(10) :
    b.append(int(input()))
a = sorted(a)
b = sorted(b)

print(sum(a[7:]), sum(b[7:]))