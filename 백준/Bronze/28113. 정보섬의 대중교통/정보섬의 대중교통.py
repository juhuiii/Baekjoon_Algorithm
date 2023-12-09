n, a, b = map(int, input().split())

if a < b :
  print("Bus")
elif b < a :
  print("Subway")
else :
  print("Anything")