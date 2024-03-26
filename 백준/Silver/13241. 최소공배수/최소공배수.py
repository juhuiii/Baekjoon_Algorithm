a, b = map(int,input().split())
c = a * b

while b :
  if a > b :
    a, b = b, a
  b = b % a

print(c // a)