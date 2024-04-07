n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

res = 0

for i in range(len(size)) :
  if size[i] % t == 0 :
    res = res + int(size[i] / t)
  else :
    res = res + int(size[i] / t) + 1

print(res)

res2 = [int(sum(size) / p), sum(size) % p]

print(*res2)