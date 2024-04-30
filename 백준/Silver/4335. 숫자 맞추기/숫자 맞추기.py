list = []

while True :
  n = int(input())
  if n == 0 :
    break
  str = input()
  if str == "too high" :
    list.append([n, 1])
  elif str == "too low" :
    list.append([n, 0])
  else :
    for i, j in list :
      if (n == i) or (int(n < i) != j) :
        print("Stan is dishonest")
        break
    else :
      print("Stan may be honest")
    list = []