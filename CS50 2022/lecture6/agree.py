from cs50 import get_string

s = get_string("Do you agree? ").lower()

if s in ["yes", "y"]:
    print("agreed")
elif s in ["no", "n"]:
    print("not agreed")
else:
    print("invalid input")