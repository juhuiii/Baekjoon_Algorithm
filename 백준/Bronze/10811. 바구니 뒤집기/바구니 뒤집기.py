n, m = map(int, input().split())
b = []
for y in range(1, n+1):
  b.append(y)


for k in range(m) :
  i, j =  map(int, input().split())
  a = b[i-1 : j]
  a.reverse()
  b[i-1:j] = a

for i in range(n):
  print(b[i], end = " ")