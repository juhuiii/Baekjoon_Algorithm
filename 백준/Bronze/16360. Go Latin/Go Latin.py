case = {"a": "as", "i": "ios", "y": "ios", "l": "les", "n": "anes", "ne": "anes", "o": "os", "r": "res", "t": "tas", "u": "us", "v": "ves", "w": "was"}
n = int(input())
for _ in range(n):
  s = input()
  l = len(s)
  res = ""
  if s[-1] in case:
    for i in range(l - 1):
        res += s[i]
    res += case[s[-1]]
  elif s[-2] + s[-1] == "ne":
    for i in range(l - 2):
        res += s[i]
    res += case[s[-2] + s[-1]]
  else:
    res = s + "us"
  print(res)