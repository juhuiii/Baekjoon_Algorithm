lists = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
lists.sort()

list2 = []
n = int(input())
for i in range(n):
  a = list(input().split())
  list2.append([a[0], a[-1]])
cow = [0 for i in range(8)]

res = 0
def check(x):
  global res
  if x == 8 and res == 0:
    for x in list2:
      if abs(cow.index(x[0]) - cow.index(x[1])) != 1:
        return
    for x in cow:
      print(x)
    res = 1
  else :
    for i in range(8):
      if not lists[i] in cow[:x]:
        cow[x] = lists[i]
        check(x+1)
check(0)