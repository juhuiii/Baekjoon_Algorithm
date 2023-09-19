l = []
ans = []
total = 0
for _ in range(8):
    l.append(int(input()))

for _ in range(5):
    total += max(l)
    ans.append(l.index(max(l))+1)
    l[l.index(max(l))] = -1
ans.sort()
print(total)
print(*ans) 