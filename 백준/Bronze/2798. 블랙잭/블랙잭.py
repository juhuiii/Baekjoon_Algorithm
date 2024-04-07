a, b = map(int, input().split())
numbers = list(map(int, input().split()))
l = set() 
m = []

for x in numbers:
    for y in numbers[1:]:
      if x == y:
        break
      for z in numbers[2:]:
        if z == x or z == y:
            break
        l.add(x + y + z)

for i in l:
    if i <= b:
        m.append(i)
print(max(m)) 