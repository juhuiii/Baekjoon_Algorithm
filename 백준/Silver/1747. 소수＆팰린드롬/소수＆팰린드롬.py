import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

N = int(input())
result = 0

for i in range(N, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if isPrime(i) == True:
            result = i
            break

if result == 0: 
    result = 1003001

print(result)