n = int(input())
l = []
count = 0

for i in range(n) :
  l.append(int(input()))

for j in range(n-1,  0, -1) :
  if l[j] <= l[j-1]:
    count += (l[j-1] -l[j] + 1)
    l[j - 1] = l[j] - 1

print(count)