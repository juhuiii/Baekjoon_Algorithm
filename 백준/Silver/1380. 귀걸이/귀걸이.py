case = 0
while True :
  n = int(input())
  if n == 0:
    break

  else :
    case += 1

  g = []
  for i in range(n) :
    g.append(input())

  r = []
  for j in range(n * 2 - 1) :
    a, b = input().split()
    r.append(int(a))

  temp = 0
  for k in range(1, n + 1) :
    if r.count(k) == 1 :
      temp = k
      break

  print(case, g[temp - 1])