a, b = input().split()

result = []
for i in range(len(b) - len(a) + 1) :
  k = 0
  for j in range(len(a)) :
    if a[j] != b[j + i] :
      k += 1
  result.append(k)
print(min(result))