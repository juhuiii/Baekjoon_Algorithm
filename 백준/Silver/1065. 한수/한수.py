n = int(input())
h = 0
for i in range(1, n + 1) :
  number = list(map(int, str(i)))
  if i < 100 :
    h += 1
  elif number[0] - number[1] == number[1] - number[2] :
    h += 1
print(h)