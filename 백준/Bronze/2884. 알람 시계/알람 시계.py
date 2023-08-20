h, m = map(int, input().split())

if 45 <= m <= 59 :
  m = m - 45

else :
  if h == 0 :
    h = 23
    m = m +15
  else :
    h = h - 1
    m = m + 15

print(h,m)