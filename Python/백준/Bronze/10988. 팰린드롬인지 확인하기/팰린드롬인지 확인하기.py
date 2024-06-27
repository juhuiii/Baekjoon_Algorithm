"""[0]

[-1]


[::-1]

a = input()
b = a[::-1]
"""

word=input()
a=0
for i in range(len(word)):
    if word[i]!=word[len(word)-i-1]:
        print("0")
        a = 0
        break
    else:
        a=1
        continue
if a==1:
    print("1")