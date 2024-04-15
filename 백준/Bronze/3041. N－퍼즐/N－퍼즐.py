p = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
cp = []
pos = {}
cnt = 0
m = 0
for i in range(4) :
  cp.append(input())

for i in range(4) :
  for j in range(4) :
    if p[i][j] != cp[i][j] and cp[i][j] != '.' :
      pos[cp[i][j]] = (i, j)

for i in range(4) :
  for j in range(4) :
    if p[i][j] in pos.keys() :
      cnt += abs(pos[p[i][j]][0] - i) + abs(pos[p[i][j]][1] - j)

print(cnt)