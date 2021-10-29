# Write function to find the roots of a quadratic equation using discriminant method
import math 

def quadratic_roots(a, b, c):
    d = b * b - 4 * a * c
    sqrt = math.sqrt(abs(d))

    if d > 0:
        r1 = (- b + sqrt) / (2 * a)
        r2 = (- b - sqrt) / (2 * a)
        print(r1, r2)
    elif d == 0:
        r1 = (- b) / (2 * a)
        r2 = r1
        print(r1, r2)
    else:
        print(str((- b) / (2 * a)) + " +i " + str(sqrt), str((- b) / (2 * a)) + " -i " + str(sqrt))
    return

a = int(input())
b = int(input())
c = int(input())
if a == 0:
    print("Wrong input")
else:
    quadratic_roots(a, b, c)
