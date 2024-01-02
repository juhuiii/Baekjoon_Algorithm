z = int(input())
l = list(map(int, input().split()))
s = 0
l2 = [] # answer 
for i in range(1, z):
    if l[i] > l[i - 1]:
      s += l[i] - l[i - 1]
      if i == z - 1 :
        l2.append(s)

    else :
      l2.append(s)
      s = 0 
      
print(max(l2)) 