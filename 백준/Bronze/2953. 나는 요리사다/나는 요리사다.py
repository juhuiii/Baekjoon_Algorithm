a=list(map(int, input().split()))
suma=a[0]+a[1]+a[2]+a[3]
b=list(map(int, input().split()))
sumb=b[0]+b[1]+b[2]+b[3]
c=list(map(int, input().split()))
sumc=c[0]+c[1]+c[2]+c[3]
d=list(map(int, input().split()))
sumd=d[0]+d[1]+d[2]+d[3]
e=list(map(int, input().split()))
sume=e[0]+e[1]+e[2]+e[3]
n=[]
n.append(suma)
n.append(sumb)
n.append(sumc)
n.append(sumd)
n.append(sume)
n.sort()
if n[4]==suma:
    print(1, suma)
elif n[4]==sumb:
    print(2, sumb)
elif n[4]==sumc:
    print(3, sumc)
elif n[4]==sumd:
    print(4, sumd)
elif n[4]==sume:
    print(5, sume)