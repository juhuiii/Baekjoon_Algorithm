i = 1
while True :
  a = input()
  b = input()
  if a == 'END' and b == 'END' :
    break
  else :
    a_new = sorted(list(a))
    b_new = sorted(list(b))

    if a_new == b_new :
      print("Case", str(i) + ": same")
    elif a_new != b_new :
      print("Case", str(i) + ": different")

    i += 1