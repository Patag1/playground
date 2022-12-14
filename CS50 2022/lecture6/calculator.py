try:
    x = int(input("x: "))
except ValueError:
    print("NaN")
    exit()

try:
    y = int(input("y: "))
except ValueError:
    print("NaN")
    exit()

print(x + y)

# ///////////////////////////////////////

from cs50 import get_int

a = get_int("a: ")
b = get_int("b: ")

div = a / b
print(div)

div_c = a // b
print(div_c)

# This is a comment
print(f"{div_c:.50f}")