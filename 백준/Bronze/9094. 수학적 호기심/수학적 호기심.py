for _ in range(int(input())):
    count = 0
    n, m = map(int, input().split()) #maybe fix
    for b in range(2, n):
        for a in range(1, b):
            if ((b*b+a*a+m)%(a*b)) == 0:
                count += 1
    print(count) 