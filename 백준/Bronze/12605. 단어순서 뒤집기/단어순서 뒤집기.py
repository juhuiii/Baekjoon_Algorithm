a = int(input())
c = []
for i in range(a) :
  b = list(input().split())
  c.append(b)
for i in range(a) :
  c[i].reverse()

for i in range(a) :
  print("Case #%d:"%(i+1), end = ' ')
  print(*c[i])