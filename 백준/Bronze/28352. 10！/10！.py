n = int(input())
result = 1
for i in range(1, n + 1) :
  result = result * i

m = result // (7 * 24 * 60 * 60)

print(m)