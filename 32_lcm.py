# import math
#
# def findinglcm(a, b):
#     a = math.lcm(a, b)
#     print("The LCM is", a)
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# findinglcm(num1, num2)

y = int(input("1st Number: "))
k = int(input("2nd Number: "))

if y>k:
    g = y
else:
    g = k
while (True):
    if g % y == 0 and g % k == 0:
        lcm = g
        break
    else:
        g = g+1
print(lcm)
