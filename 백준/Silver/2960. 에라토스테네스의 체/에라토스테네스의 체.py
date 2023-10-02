a, b =map(int, input().split())
arr = []
for i in range(2, a + 1) :
  arr.append(i)

count = 0
remove_num = []

while arr :
  number = arr[0]
  remain_num = []

  for i in arr :
    if i % number == 0 :
      remove_num.append(i)
      count += 1

    else :
      remain_num.append(i)

  arr = remain_num

  if b <= count :
    break

print(remove_num[b-1])