a  = int(input())
b = 10
while a > b :
  if a % b >= b // 2 :
    a += b
  a = a - (a % b)
  b = b * 10
print(a)