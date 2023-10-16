a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 + a2 + a3 == 180:
    if a1 == a2 == a3:
        print("Equilateral")
    elif a1 == a2 and a1 != a3:
        print("Isosceles")
    elif a2 == a3 and a2 != a1:
        print("Isosceles")
    elif a1 == a3 and a1 != a2:
        print("Isosceles")
    elif a1 != a2 and a1 != a3 and a2 != a3:
        print("Scalene")
else:
    print("Error")