a, b, c = map(int, input().split())

a = a + b
by = 0

while 1 :
  by = by  + (a // c)
  a = a // c + a % c

  if a < c :
    break
print(by)