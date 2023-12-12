a, b = map(int, input().split())
l = list(map(str, input().split()))
l2 = []
while True:
    l2 = []
    if l == []:
        break
    else:
        count = 0
        for i in l:
            if count + len(i) <= b:
                count += len(i)
                l2.append(i)
            else:
                break
        for i in l2:
            l.remove(i)
        l2 = ' '.join(l2)
        print(l2)