K = int(input())
string = list(input())

answer = []
c = 0

for i in range(K - 1) :
  if string[i] != string[i + 1]:
    answer.append(c + 1)
    c = 0
  elif string[i] == string[i + 1]:
    c += 1

answer.append(c + 1)

if len(answer) == 1:
  print(0)

else :
  answer2 = []
  for j in range(len(answer) - 1):
    answer2.append(min(answer[j], answer [j + 1]))
  print(max(answer2) * 2)