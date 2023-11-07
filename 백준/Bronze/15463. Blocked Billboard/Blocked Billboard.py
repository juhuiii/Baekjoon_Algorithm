a = []

for y in range(2001):
  b = []
  for x in range(2001):
    b.append(0)
  a.append(b)

for i in range(3):
  x1, y1, x2, y2 = map(int, input().split())
  for x in range(x1 + 1000, x2 + 1000):
    for y in range(y1 + 1000, y2 + 1000):
      if i < 2 :
        a[y][x] = 1
      else :
        a[y][x] = 0

count = 0
for y in range(len(a)):
  for x in range(len(a[y])):
    if a[y][x] == 1:
      count+= 1

print(count)
