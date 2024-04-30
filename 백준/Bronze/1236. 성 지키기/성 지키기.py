n, m = map(int, input().split())
c = []

for i in range(n) :
  c.append(input())

a, b = 0, 0

for i in range(n) :
  if "X" not in c[i] :
    a += 1
for j in range(m) :
  if "X" not in [c[i][j] for i in range(n)] :
    b += 1

print(max(a, b))