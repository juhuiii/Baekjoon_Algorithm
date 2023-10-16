import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
    _ = input()  # 공백
    N = int(input())
    candy = 0
    for _ in range(N):
        candy += int(input())
    if candy % N == 0:
        print("YES")
    else:
        print("NO")