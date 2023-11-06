j = list(map(int, input()))

if sum(j[:len(j) // 2]) == sum(j[len(j) //2 :]):
  print("LUCKY")
else:
  print("READY")