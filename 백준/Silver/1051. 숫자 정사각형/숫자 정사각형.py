n, m = map(int,input().split())
a = []
for i in range(n) :
  a.append(list(map(int, input())))
b = [] # result
length = min(n, m)

for i in range(n) :
  for j in range(m) :
    for k in range(length) :
      if ((i + k) < n ) and (j + k < m) :
        if(a[i][j] == a[i + k][j] == a[i][j + k] == a[i + k][j + k]) :
          b.append((k + 1) * (k + 1))
print(max(b))