def main():
    for i in range(n):
        print("#")

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                break
        except ValueError:
            print("NaN")
    return n

# ///////////////////////////////////////

for i in range(4):
    print("#", end="")

print()

# print("#" * n)

# ///////////////////////////////////////

for x in range(4):
    for y in range(4):
        print("#", end="")
    print()

for a in range(4):
    print("#" * 4)