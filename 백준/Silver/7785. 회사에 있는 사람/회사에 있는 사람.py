import sys
input = sys.stdin.readline 

name = set()

for i in range(int(input())) :
  a, b = input().split()
  if b == 'enter' :
    name.add(a)
  elif b == 'leave':
    name.remove(a)
new_name = sorted(name, reverse = True)

print(*new_name, sep = '\n')