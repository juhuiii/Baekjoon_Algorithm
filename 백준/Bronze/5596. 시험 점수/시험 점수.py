s=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
if sum(s)>sum(t):
    print(sum(s))
else:
    print(sum(t))