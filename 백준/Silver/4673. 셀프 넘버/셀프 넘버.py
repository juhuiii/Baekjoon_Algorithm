def selfnumber(num):
  selfnumber = num
  while num != 0 :
    selfnumber += num % 10
    num //= 10
  return selfnumber

answer = []
for i in list(range(1, 10001)) :
  answer.append(selfnumber(i))
  if i not in answer :
    print(i)