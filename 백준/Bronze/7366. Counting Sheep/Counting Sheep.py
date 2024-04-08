n = int(input())
for i in range(n):
    m = int(input())
    l = list(map(str, input().split()))
    print("Case {}: This list contains {} sheep.".format(i+1, l.count('sheep'))) 
    print()