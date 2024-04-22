N = int(input())
pocket = []
dogam = []
for i in range(N):
    P  = str(input())
    K, M = map(int,input().split())
    evo = 0
    while True :
        if K > M :
            break
        else :
            M = M-K+2
            evo += 1
    pocket.append([P,evo,i])

result = 0
for i in range(N):
    result += pocket[i][1]
print(result)

last = sorted(pocket, key=lambda x:(-x[1], x[2]) )
print(last[0][0])