n = int(input())
l = []
for i in range(n):
    s = str(input())
    l.append((s.count('for') + s.count('while')))
print(max(l))