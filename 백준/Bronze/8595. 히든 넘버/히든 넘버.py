n = int(input())
l = input()
hidden = ''
hidden_number = 0


for i in l :
  if '0' <= i and i <= '9' :
    hidden += i
  elif hidden != '' :
    hidden_number += int(hidden)
    hidden = ''

if hidden != '' :
  hidden_number += int(hidden)

print(hidden_number)