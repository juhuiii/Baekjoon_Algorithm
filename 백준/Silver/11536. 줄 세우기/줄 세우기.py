n = int(input())
name = []

for i in range(n) :
  name.append(input())

if name == sorted(name, reverse = True) :
  print("DECREASING")
elif name == sorted(name) :
  print("INCREASING")
else :
  print("NEITHER")