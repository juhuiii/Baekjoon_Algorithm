s = input()
original = []
i = 0

while i < len(s) :
  if s[i] in ('a', 'e', 'i', 'o', 'u') :
    original.append(s[i])
    i += 3
  else :
    original.append(s[i])
    i += 1

print(''.join(original))