a, b, c = map(int, input().split())

min_num = 0
max_num = 0

if c - b == 1 and b - a == 1 :
    min_num += 0
elif c - b == 2 or b - a == 2 :
    min_num += 1
else :
    min_num += 2
    
# max_num : ( (max - 2) - mid ) + 1 = max -2 - mid + 1 = max - mid - 1
if c - b > b - a :
    max_num += (c - b) - 1
else :
    max_num += (b - a) - 1
print(min_num)
print(max_num)