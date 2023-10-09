a, b, c = map(int, input().split())
arrive = []
leave = []
truck_count = 0
cost = 0
for i in range(3):
    x, y = map(int, input().split())
    arrive.append(x)
    leave.append(y)
for i in range(max(leave)):
    if arrive.count(i) >= 1:
        truck_count += arrive.count(i)
    if leave.count(i) >= 1:
        truck_count -= leave.count(i)
    if truck_count == 1:
        cost += a
    if truck_count == 2:
        cost += 2 * b
    if truck_count == 3:
        cost += 3 * c
print(cost) 