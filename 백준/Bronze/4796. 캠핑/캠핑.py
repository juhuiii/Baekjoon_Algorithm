count = 0
while 1 :
  count += 1
  l, p, v = map(int, input().split())
  if l == 0 and p == 0 and v == 0 :
    break

  g = v // p
  a = v % p

  if l < a :
    a = l
  print("Case %d: %d" %(count, g * l + a))