a = input()
b = 10
for i in range(1, len(a)) :
    if a[i] == a[i - 1]:
        b += 5
    else :
        b+= 10
print(b)