x = int(input())
y = 1 
for i in range(x-1,-1, -1):
  print(" "*i+"*"*y)
  y = y + 2
u = 1
for j in range(1,x ,1):
  print(" "*j+"*"*((2 * (x - 1)) - u))
  u = u + 2
