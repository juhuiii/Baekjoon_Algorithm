a = int(input())
for i in range(a):
  t = []
  b = int(input())
  for j in range(b):
    t.append(int(input()))
  if t.count(max(t)) > 1:
    print('no winner')
  else:
    y = max(t)
    
    if sum(t)-max(t) >= y:
      print('minority winner',t.index(y)+1)
    else:
      print('majority winner',t.index(y)+1)