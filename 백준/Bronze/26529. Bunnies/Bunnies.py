z = int(input())
for i in range(z):
    a = 0
    b = 1
    n = int(input())
    for j in range(n):
        m = a + b
        if a <= b:
            a = m
        else:
            b = m 
    if a >= b:
        print(a)
    else:
        print(b)