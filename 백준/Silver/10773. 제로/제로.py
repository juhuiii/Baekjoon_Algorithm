num=[]
for i in range(int(input())):
    k=int(input())
    if k!=0:
        num.append(k)
    else:
        del num[len(num)-1]
print(sum(num))