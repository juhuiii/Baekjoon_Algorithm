n=int(input())
a=0
print("*"*n)
for i in range(n-1):
    print(" "*a,"*"*(n-1))
    a=a+1
    n=n-1