n = int(input())
a = list(map(int,input().split()))
plus = 0
sum = 0
for i in range(n):
    if a[i] == 1:
        plus += 1
    else:
        plus = 0
    sum += plus
    
print(sum)