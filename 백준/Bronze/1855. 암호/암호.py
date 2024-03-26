c = int(input())
word = input()
m = len(word)
r = m // c

a = ''

b = [[0] * c for i in range(r)]
for i in range(r) :
  for j in range(c) :
    b[i][j] = word[c * i + j]
  if i % 2 == 1 :
    b[i] = b[i][::-1]

for i in range(c) :
  for j in range(r) :
    a += b[j][i]

print(a)