a = int(input())
b = int(input())
print(a)
print(b)
for i in range(len(str(b))):
    print(a*int(str(b)[len(str(b))-1-i]))
print(a*b)
