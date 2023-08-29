n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    A = sorted(a)
    B = sorted(b)
    if A == B:
        print(a, "&", b, "are anagrams.")
    else:
        print(a, "&", b, "are NOT anagrams.") 