import sys 
input = sys.stdin.readline

n, k = map(int, input().split())

dia = []
for _ in range(n) :
  dia.append(int(input()))
dia.sort()

max_count = 1
for i in range(n) :
  count = 1
  for j in range(i + 1, n) :
    if dia[j] > dia[i] + k :
      break
    count += 1
  max_count = max(max_count, count)

print(max_count)