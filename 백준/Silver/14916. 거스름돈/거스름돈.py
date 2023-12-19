a = int(input())
r = 0 
while True :
  if a % 5 == 0 :
    r += a // 5
    break
  else :
    a -= 2
    r += 1

  if a < 0 :
    break

if a < 0 :
  print(-1)
else  :
  print(r)