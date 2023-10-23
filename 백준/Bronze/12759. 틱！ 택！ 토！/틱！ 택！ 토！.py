n = int(input())
list = list(list("" for _ in range(3)) for _ in range(3))

win = 0

while 1 :
  x, y = map(int, input().split())
  x, y = x - 1, y -1

  if n == 1 :
    list[x][y] = "O"
    n = 2
  elif n == 2:
    list[x][y] = "X"
    n = 1

  for i in range(3):
    if(list[i][0] == list[i][1] == list[i][2]) and (list[i][0] != "") :
      if list[i][0] == "O":
        win = 1
      else :
        win = 2

  for i in range(3):
    if(list[0][i] == list[1][i] == list[2][i]) and (list[0][i] != "") :
      if list[0][i] == "O":
        win = 1
      else :
        win = 2

  if(list[0][0] == list[1][1] == list[2][2]) and (list[1][1] != "") :
    if list[1][1] == "O":
      win = 1
    else :
      win = 2

  if(list[0][2] == list[1][1] == list[2][0]) and (list[1][1] != "") :
    if list[1][1] == "O":
      win = 1
    else :
      win = 2

  if win != 0:
    break

  else :
    cnt = 0
    for row in list :
      for el in row :
        if el != "" :
          cnt += 1
    if cnt == 9 :
      win = 0
      break
print(win)