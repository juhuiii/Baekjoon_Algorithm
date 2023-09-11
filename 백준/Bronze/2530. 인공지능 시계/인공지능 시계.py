x, y, z = map(int, input().split())
a = int(input())  # second

z += a
y += z // 60
x += y // 60

z %= 60
y %= 60
x %= 24

print(x, y, z)