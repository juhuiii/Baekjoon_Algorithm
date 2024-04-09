while 1:
  y = []
  a = int(input())
  if a == 0:
    break
    
  for i in range(a):
    k = input()

    y.append(k)

  y.sort(key = str.lower)
  print(y[0]) 