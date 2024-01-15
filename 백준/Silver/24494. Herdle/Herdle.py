alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

green = 0
total = 0

alp1 = [0] * 26
alp2 = [0] * 26

a = []
for i in range(3) :
  a.append(input())

b = []
for i in range(3) :
  b.append(input())

for i in range(3) :
  for j in range(3) :
    if a[i][j] == b[i][j] :
      green += 1

for aa in a :
  for aaa in aa :
    alp1[alp.index(aaa)] += 1

for bb in b :
  for bbb in bb :
    alp2[alp.index(bbb)] += 1

for i in range(26) :
  if alp1[i] :
    total += min(alp1[i], alp2[i])

print(green)
print(total - green)