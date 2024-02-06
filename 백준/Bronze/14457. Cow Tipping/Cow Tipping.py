n = int(input())
cow = []
temp = 0
for i in range(n) :
  c = list(map(int, input()))
  cow.append(c)

for j in range(n - 1 , -1, -1) :
  for k in range(n - 1, -1, -1) :
    if cow[j][k] == 1 :
      temp += 1
      for a in range(j + 1) :
        for b in range(k + 1) :
          if cow[a][b] == 0 :
            cow[a][b] = 1
          else :
            cow[a][b] = 0

print(temp)