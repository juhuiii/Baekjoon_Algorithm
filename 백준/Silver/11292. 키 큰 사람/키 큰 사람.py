while True:
    n = int(input())
    if n == 0:
        break
    else:
        l = []
        l2 = []
        for i in range(n):
            a, b = map(str, input().split()) 
            l.append(a)
            l2.append(float(b))
        l3 = []
        if l2.count(max(l2)) > 1:
            for i in range(len(l2)):
                if l2[i] == max(l2):
                    l3.append(l[i])
            print(*l3)
        else:
            print(l[l2.index(max(l2))])