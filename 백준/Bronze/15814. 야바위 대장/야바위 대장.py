w = list(input())
for i in range(int(input())) :
    a, b = map(int, input().split(' '))
    w[a], w[b] = w[b], w[a]
print(''.join(w))