n=[int(x) for x in input().split()]
n.sort()

for i in input():
    print(n[ord(i)-65],end=" ")