n = int(input())
q = 2
while 1 :
  if (n == 1 or n == 2) :
    print(n)
    break
  q *= 2
  if (q >= n) :
    print((n - (q // 2)) * 2)
    break