num = int(input("Enter number of digits wanted: "))
x = 0
y = 1
print(x)
print(y)
for c in range(2, num):
    z = x+y
    print(z)
    x = y
    y = z
print()

