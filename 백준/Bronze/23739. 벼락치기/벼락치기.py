ch = []
limit = 30
kan = 0
tot = 0

n = int(input())
for i in range(n) :
  time = int(input())
  ch.append(time)

for j in range(n) :
  if limit <= 0 :
    limit = 30
  kan = ch[j] / 2
  if limit - ch[j] >= 0:
    limit = limit - ch[j]
    tot += 1

  elif limit - ch[j] <= 0 and limit >= kan :
    limit = 0
    tot += 1

  elif limit - ch[j] <= 0 and limit < kan :
    limit = 0
    continue

print(tot)