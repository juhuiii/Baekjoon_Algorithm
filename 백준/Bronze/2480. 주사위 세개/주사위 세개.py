a,b,c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b!=c:
    print(1000+a*100)
elif a==c!=b:
    print(1000+a*100)
elif a!=b==c:
    print(1000+b*100)
elif a!=b!=c:
    t=[]
    t.append(a)
    t.append(b)
    t.append(c)
    t.sort()
    print(t[2]*100)