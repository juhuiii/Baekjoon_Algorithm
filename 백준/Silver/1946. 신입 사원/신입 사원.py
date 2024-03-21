import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
  n = int(input())
  arr = [list(map(int, input().split())) for _ in range(n)]
  arr.sort()
  
  p = 1
  maxgrade = arr[0][1]
  for i in range(1, n) :
    if maxgrade > arr[i][1] :
      p += 1
      maxgrade = arr[i][1]
  print(p)