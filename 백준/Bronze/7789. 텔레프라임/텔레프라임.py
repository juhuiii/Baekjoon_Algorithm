a, b = map(int, input().split())
n = 10 ** len(str(a))
n = b * n + a
s = 0
for i in range(1, a + 1):
    if a % i == 0:
        s += 1
for i in range(1, n + 1):
    if n % i == 0:
        s += 1
        
if s == 4 :
    print("Yes")
else:
    print("No") 