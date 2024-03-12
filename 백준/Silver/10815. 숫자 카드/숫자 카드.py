import sys
input = sys.stdin.readline
N = int(input())
card_N = set(map(int, input().split()))
M = int(input())
check_M = list(map(int, input().split()))

for num in check_M:
    if num in card_N:
        print(1, end=' ')
    else:
        print(0, end=' ')