num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
if line % 2 == 0:
    u_n = num
    d_n = line - num + 1
else:
    u_n = line - num + 1
    d_n = num

print(u_n,'/',d_n, sep="")