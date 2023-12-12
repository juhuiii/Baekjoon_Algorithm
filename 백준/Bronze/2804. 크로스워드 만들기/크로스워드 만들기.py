a, b = input().split()

for i in range(len(a)) :
  if a[i] in b :
    ok = a[i]
    ok_i = i
    break

for j in range(len(b)) :
  if b[j] == ok:
    bbang_i = j
    break

result = ['.'] * len(a)
for k in range(len(b)) :
  result[ok_i] = b[k]

  if k == bbang_i :
    print(a)
  else :
    print(''.join(map(str, result)))