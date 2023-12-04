n = int(input())
s = 1
total = 0
count = 0
while True:
    if s + total > n:
        print(count)
        break
    total += s
    s += 1
    count += 1