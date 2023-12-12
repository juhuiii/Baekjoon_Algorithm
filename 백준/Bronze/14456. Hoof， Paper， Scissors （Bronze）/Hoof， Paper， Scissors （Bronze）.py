n = int(input())
count1 = 0
count2 = 0
for i in range(n) :
  a, b = map(int, input().split())

  if (a == 1 and b ==2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    count1 += 1
  elif (a == 1 and b == 3) or (a == 3 and b == 2) or (a == 2 and b == 1) :
    count2 += 1

print(max(count1, count2))