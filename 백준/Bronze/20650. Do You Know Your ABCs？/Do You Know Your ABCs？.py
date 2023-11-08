k = list(map(int, input().split()))

k.sort()
abc = k[6]
a = k[0]
b = k[1]
c = abc - a - b
print(a, b, c)