n=list(map(int, input().split()))
a=1
sum=0
for i in range(0,5):
    a=a*n[i]**2
    sum=sum+a
    i=i+1
    a=1
print(sum%10)