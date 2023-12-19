a, b = map(int, input().split())
q, w, e, r = map(int, input().split())

k = 0
for i in range(a) :
  t = input()
  k += t.count("P")

h = e * r

if k == h :
  print(0)
else :
  print(1)