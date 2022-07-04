g = int(input("Enter Number: "))
for y in range(1, g+1):
    if g % y == 0:
        factor = y
        print(factor)
