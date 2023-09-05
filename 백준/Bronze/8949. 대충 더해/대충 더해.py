a, b = map(str, input().split())

mlen = 0

if len(a) > len(b) :
  mlen = len(a)
  b = '0' * (len(a) - len(b)) + b

elif len(a) < len(b) :
  mlen = len(b)
  a = '0' * (len(b) - len(a)) + a

else :
  mlen = len(b)

c = ""
for i in range(mlen) :
  c += str(int(a[i]) + int(b[i]))

print(c)