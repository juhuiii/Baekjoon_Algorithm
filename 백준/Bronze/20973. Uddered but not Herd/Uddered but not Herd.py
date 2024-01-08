l = []
s2 = str(input())
for i in s2:
    l.append(i)
s = str(input())
count = 1
check = ''
for i in range(len(s)):
    if s[i] != ' ':
        if check == '':
            check = s[i]
        else:
            if l.index(s[i]) <= l.index(check):
                count += 1
            check = s[i]
print(count)