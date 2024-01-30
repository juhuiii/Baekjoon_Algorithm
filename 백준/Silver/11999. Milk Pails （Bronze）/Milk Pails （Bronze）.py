import sys 
input = sys.stdin.readline

x, y, m = map(int, input().split()) # x < y < m
max = 0
for i in range(m // x + 1) :
  for j in range(m // y + 1) :
    total = i * x + j * y
    if max < total <= m : 
      max = total

print(max)