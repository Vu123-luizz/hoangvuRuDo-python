import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print("Nghiệm x =", -c/b)
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("2 nghiệm:", x1, x2)
    elif delta == 0:
        print("Nghiệm kép:", -b/(2*a))
    else:
        print("Vô nghiệm")
