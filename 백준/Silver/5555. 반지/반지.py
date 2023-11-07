w = input()
count = 0
for i in range(int(input())):
    ring = input()
    if w in ring * 2:
        count += 1
print(count)