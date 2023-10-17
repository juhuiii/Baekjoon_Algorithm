n, m = map(int, input().split())

a = []
b = []
for i in range(n) :
  road, spped = map(int, input().split())
  for j in range(road) :
    a.append(spped)

for i in range(m) :
  road, spped = map(int, input().split())
  for j in range(road) :
    b.append(spped)

c = 0

for i in range(100) :
  if b[i] - a[i] > c :
    c = b[i] - a[i]
print(c)