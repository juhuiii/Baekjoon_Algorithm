for i in range(int(input())):
    y = int(input())
    n = list(map(int, input().split()))
    sum = 0
    n.sort()
    for i in range(len(n)):
        if i != len(n) - 1:
            if n[i] > n[i+1]:
                sum += n[i]-n[i+1]
            else:
                sum += n[i+1] - n[i]
    if n[0] > n[-1]:
        sum += n[0] - n[-1]
    else:
        sum += n[-1] - n[0]
    print(sum)