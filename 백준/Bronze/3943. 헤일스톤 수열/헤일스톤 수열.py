import sys
input = sys.stdin.readline

for i in range(int(input())) :
  a = int(input())
  num = []
  while 1 :
    if 1 in num :
      break
    num.append(a)
    if a % 2 == 0 :
      a //= 2
    else :
      a = a * 3 + 1
  print(max(num))