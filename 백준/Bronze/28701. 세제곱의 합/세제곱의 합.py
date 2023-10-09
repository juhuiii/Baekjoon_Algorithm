n = int(input())
sum1 = 0
sum3 = 0
for i in range(1, n+1):
    sum1 += i
print(sum1)
print(sum1 ** 2)
for k in range(1, n+1):
    sum3 += k**3
print(sum3)