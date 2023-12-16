STR, DEX, INT, LUK, N = map(int ,input().split())

total = STR + DEX + INT + LUK
t = N * 4

if t > total :
  print(t - total)

else :
  print(0)