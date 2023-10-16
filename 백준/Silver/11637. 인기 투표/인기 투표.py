z = int(input())
for i in range(z):
    l = []
    a = int(input())
    for i in range(a):
        b = int(input())
        l.append(b)
    if l.count(max(l)) >= 2 :
        print("no winner")
    else:
        if max(l) > int(sum(l)/2):
            print("majority winner", l.index(max(l))+1)
        else:
            print("minority winner", l.index(max(l))+1)    