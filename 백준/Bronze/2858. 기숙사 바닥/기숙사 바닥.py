r, b = map(int, input().split())
lpw = (r + 4) // 2
lw = r + b

for i in range(1, lpw):
  if(lpw - i) * i == lw :
    print(max(i, lpw - i), min(i, lpw - i))
    break