k = int(input())
for _ in range(k):
    count = 0
    n, m = map(int, input().split()) #maybe fix
    for b in range(2, n):
        #print()
        #print("B is now equal to", b)
        for a in range(1, b):
            #print("A is now equal to", a)
            if ((b*b+a*a+m)/(a*b))%1 == 0:
                #print("count is now added")
                count += 1
    print(count) 