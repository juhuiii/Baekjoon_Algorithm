a = int(input())
for i in range(a) :
  h, w, n = map(int, input().split())
  f = n % h
  r = n//h+1
  if f == 0 :
    r -= 1
    f = h
  print(f * 100 + r)