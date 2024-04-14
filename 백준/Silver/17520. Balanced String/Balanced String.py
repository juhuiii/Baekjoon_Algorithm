n = int(input())
res = 1
c = (n+1) // 2
for i in range(c) :
  res = (res * 2) % 16769023
print(res)