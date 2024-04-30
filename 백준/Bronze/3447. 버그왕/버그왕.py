while True :
  try :
    str = input()
    while "BUG" in str :
      str = str.replace("BUG", "")
    print(str)

  except EOFError:
    break