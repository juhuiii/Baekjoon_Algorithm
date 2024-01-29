import sys 
input = sys.stdin.readline

n = int(input())
l = [float(input()) for _ in range(n)]

for i in sorted(l) [:7] :
  print(f'{i:.3f}')