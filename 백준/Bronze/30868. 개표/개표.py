t = int(input())
for i in range(t) :
  n = int(input())
  x = n // 5
  y = n % 5

  for j in range(x) :
    print("++++", end = " ")

  for k in range(y) :
    print("|", end = "")
  print("")