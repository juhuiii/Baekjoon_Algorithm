a = int(input())
teamd = 0
teamp = 0
for i in range(a) :
  score = input()
  if score == "D" :
    teamd += 1
  elif score == "P" :
    teamp += 1
  if abs(teamd - teamp) == 2 :
    break
print(f"{teamd}:{teamp}")