n, m = map(int, input().split())
stamp = []
prize = m - 1

for i in range(m) :
  x, y = map(int, input().split())
  if x < n :
    stamp.append(n - x)
  else :
    prize -= 1

stamp.sort()
total = 0

if prize > 0 :
  for i in range(prize) :
    total += stamp[i]

print(total)