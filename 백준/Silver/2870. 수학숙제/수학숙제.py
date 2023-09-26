m = int(input())
nums = ['0','1','2','3','4','5','6','7','8','9']
letters = []
result = []

for i in range(m) :
  letters.append(input())

count = ''
l =[]

for letter in letters :
  for i in letter :
    if i in nums :
      count += i
    else :
      if count :
        l.append(count)
        count = ''
  if count :
    l.append(count)
    count = ''

for j in l :
  result.append(int(j))

result.sort(reverse=False)

for k in result :
  print(k)