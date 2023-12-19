n = int(input())
room = []

for i in range(n) :
  room.append(list(map(str, input())))

temp = [0, 0]
for i in range(n) :
  a, b = 0, 0
  for j in range(n) :
    if room[i][j] == '.' :
      a += 1
    elif room[i][j] == 'X' :
      if a >= 2 :
        temp[0] += 1
      a = 0

    if room[j][i] == '.':
      b += 1
    elif room[j][i] == 'X' :
      if b >= 2 :
        temp[1] += 1
      b = 0

    if j == n - 1 :
      if a >= 2 :
        temp[0] += 1
      if b >= 2 :
        temp[1] += 1

print(' '.join(map(str, temp)))