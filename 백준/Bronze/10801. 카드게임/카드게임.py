x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = 0
b = 0
for i in range(10):
    if x[i] > y[i]:
        a += 1
    elif x[i] < y[i]:
        b += 1
print('A' if a > b else 'B' if a < b else 'D')