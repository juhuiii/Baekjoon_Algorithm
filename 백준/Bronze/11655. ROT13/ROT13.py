n = input()

for i in n :
  if 65 <= ord(i) <= 77 or 97 <= ord(i) <= 109 :
    print(chr(ord(i) + 13), end = '')
  elif 110 <= ord(i) <= 122 :
    print(chr(97 + ord(i) - 110), end = '')
  elif 78 <= ord(i) <= 90:
    print(chr(65 + ord(i)  - 78), end = '')
  else :
    print(i, end = '')