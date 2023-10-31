n = int(input())
l = []
l2 = []
for _ in range(n):
    s = str(input())
    l.append(s)
for i in l:
    k = i[::-1]
    if l.count(k) != 0:
        l2.append(str(len(i)))
        l2.append(i[int((len(i) / 2) - 0.5)])
        print(' '.join(l2))
        break 