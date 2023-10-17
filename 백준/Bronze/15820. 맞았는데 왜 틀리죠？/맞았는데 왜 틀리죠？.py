a, b = map(int, input().split())

c = True
for i in range(a):
  x, y  = map(int, input().split())
  if x != y :
    c = False

d = True
for i in range(b) :
  x, y  = map(int, input().split())
  if x != y :
    d = False

if c and d :
  print("Accepted")
elif c and not d :
  print("Why Wrong!!!")
else :
  print("Wrong Answer")