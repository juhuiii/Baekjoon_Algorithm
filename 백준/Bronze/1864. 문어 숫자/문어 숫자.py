oct = ['-',0, '\\', 1, '(', 2, '@', 3, '?', 4, '>', 5, '&', 6, '%', 7, '/',(-1)]
while 1:
  ans = 0
  a = input()
  if a == '#':
    break
  else:
    for i in range(len(a)):
      ans += oct[oct.index(a[i])+1] * (8**(len(a)-i-1))
  print(ans)