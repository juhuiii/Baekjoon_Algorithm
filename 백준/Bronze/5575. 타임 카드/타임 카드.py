for i in range(3) :
  a, b, c, d, e, f = map(int, input().split())

  a1 = a*3600 + b * 60 + c
  a2 = d * 3600 + e * 60 + f
  a3 = a2 - a1
  print(a3 // 60 // 60 % 24, a3 // 60 % 60, a3 % 60)