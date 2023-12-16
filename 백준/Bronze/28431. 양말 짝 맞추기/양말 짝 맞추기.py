socks = []

for i in range(5) :
  n = int(input())

  if n in socks :
    socks.remove(n)
  else :
    socks.append(n)

print(socks[0])