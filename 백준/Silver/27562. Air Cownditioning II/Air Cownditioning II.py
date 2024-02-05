from itertools import combinations

n, m = map(int, input().split())
farm = [0] * 100
total = 1000000
for i in range(n) :
  a, b, c = map(int, input().split())
  for i in range(a - 1, b) :
    farm[i] += c

air = [[0 for i in range(4)] for j in range(m)] 

for i in range(m) :
  air[i][0], air[i][1], air[i][2], air[i][3] = map(int, input().split())

ans = [int(i) for i in range(0, m)]
for i in range(1, m + 1):
  com = list(combinations(ans, i))
  for j in range(len(com)) :
    combi = com[j]
    farm_new = farm[:]
    cost = 0
    for k in combi :
      cost += air[k][3]
      for l in range(air[k][0] -1, air[k][1]) :
        farm_new[l] -= air[k][2]
        if farm_new[l] < 0 :
          farm_new[l] = 0
    if farm_new.count(0) == 100:
      if total > cost :
        total = cost
print(total)
