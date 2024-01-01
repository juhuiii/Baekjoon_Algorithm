n = int(input())
l = [] # working time

l3 = []
l4 = [0] * 1000
for i in range(n):
    a, b= map(int, input().split())
    l.append((a, b))
    for i in range(a, b):
      l4[i] += 1
    

count = 0
for j in l :
    a = j[0] # start
    b = j[1] #end
    for i in range(a, b) :
      l4[i] -= 1

    time = 0
    for m in l4 :
      if m > 0 :
        time += 1
    count = max(time, count)
    for n in range(a, b) :
      l4[n] += 1
  
print(count)