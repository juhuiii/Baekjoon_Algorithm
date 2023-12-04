for i in range(int(input())) :
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  a.sort()
  b.sort()

  pair = 0
  cnt = 0
  for j in range(n) :
    while True :
      if cnt == m  or a[j] <= b[cnt] :
        pair += cnt
        break
      else :
        cnt += 1

  print(pair)