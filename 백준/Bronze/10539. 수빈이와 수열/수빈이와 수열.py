n = int(input())
l = []
l2 = list(map(int, input().split()))
for i in range(len(l2)):  
    if i == 0:
        l.append(l2[0])
    else:
        l.append(l2[i] * (i+1) - sum(l))
print(*l)