a = input()
b = ['pi','ka','chu']

for i in b:
  if i in a:
    a = a.replace(i,'0')
for i in range(len(a)):
  if a[i] != '0':
    print('NO')
    break
else:
  print('YES')