o = 0
a = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
g = []
b = list(input().split())
for i in b:

    if i in a:
      if i == b[0]:
        g.append(i[0].upper())
        continue
    else:
        g.append(i[0].upper())
print(''.join(g))