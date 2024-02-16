n = input()
l = list(map(int, input().split()))

odd = 0
even = 0

for i in l :
    if i % 2 == 0 :
        even += 1
    else :
        odd += 1
check = 0
even_g = even
odd_g = odd

while odd_g > even_g :
    odd_g -= 2
    even_g += 1

if even_g >= odd_g + 1 :
    check = 2 * odd_g + 1
elif even_g == odd_g :
    check = 2 * odd_g
print(check)