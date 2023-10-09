n = int(input())
for i in range(n):
    b = sum(map(int, str(i))) + i

    if b == n :
      print(i)
      break

else :
  print(0)