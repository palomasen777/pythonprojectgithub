v = int(input("Enter a number between 1-10: "))
for x in range(v):
    for j in range(-6, -x):
        print(" ", end="")
    for s in range(x+1):
        print("* ", end="")
    print()
for i in range(v, 0):
    for k in range(v - i):
        print(" ", end=" ")

    for k in range(2 * i - 1):
        print("* ", end=" ")
    print()

