a, b = map(str, input().split())
for i in range(len(a)) :
  if a[i] in b :
    same = a[i]
    a_i = i
    break

for j in range(len(b)) :
  if b[j] == same :
    b_i = j
    break

result = ['.'] * len(a)
for k in range(len(b)) :
  result[a_i] = b[k]

  if k == b_i :
    print(a)
  else :
    print(''.join(map(str, result)))