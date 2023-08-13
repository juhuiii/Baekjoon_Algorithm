a = int(input())
b = int(input())

print(a * (b%10))          #3
print(a * ((b%100) // 10))   #4
print(a * (b//100))        #5
print(a * b)               #6