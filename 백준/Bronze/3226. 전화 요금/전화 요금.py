n = int(input())
c = 0
for i in range(n) :
  s = input()
  s = s.replace(':', ' ')
  h, m, time = map(int, s.split())
  eh, em = h, 0

  if time + m >= 60:
    em = time + m - 60
    eh = h + 1
    if eh > 23 :
      eh = 0
  else :
    em = time + m

  if (eh == 7 or eh == 19) and m >=em and em != 0 :
    if eh == 7 :
      c += (time - em) * 5 + em * 10
    elif eh == 19:
      c += (time - em) * 10 + em * 5
  else :
    if 7 <= h <= 18 :
      c += time *10
    else :
      c += time * 5
print(c)