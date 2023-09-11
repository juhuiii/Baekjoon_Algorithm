N, M = map(int, input().split())

arr = list(range(N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

print(*arr[1:])