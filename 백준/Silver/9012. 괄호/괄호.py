n = int(input())
for i in range(n):
    s = str(input())
    l = []
    for i in s:
        l.append(i)
    if len(s) % 2 == 1:
        print('NO')
    else:
        test = 0
        while True:
            if l.count('(') > 0 and l.count(')') > 0:
                if l.index('(') > l.index(')'):
                    test = 1
                    break
            elif l.count('(') == 0 and l.count(')') == 0:
                break
            else:
                test = 1
                break
            l.remove('(')
            l.remove(')')
        if test == 1:
            print("NO")
        else:
            print("YES") 