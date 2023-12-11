n = int(input())
s = input()
res = []
for i in range(n) :
  for j in range(n) :
    cnt = 0
    for k in range(i + 1, n) :
      if s[i : i + j] == s[k : k + j] :
        cnt = 1
      if cnt == 1 :
        res.append (j + 1)
print(max(res))