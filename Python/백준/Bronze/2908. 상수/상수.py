a,b=map(int, input().split())
a1=a//100
a2=(a%100)//10
a3=(a%100)%10
b1=b//100
b2=(b%100)//10
b3=(b%100)%10
newa=(a3*100)+(a2*10)+a1
newb=(b3*100)+(b2*10)+b1
if newa<newb:
    print(newb)
elif newb<newa:
    print(newa)