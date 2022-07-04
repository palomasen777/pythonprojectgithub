def addTwoNumbers(num1, num2):
    a = num1 +num2
    print(a)
    return a
num1 = int(input('Num1? = '))
num2 = int(input('Num2? = '))
z = addTwoNumbers(num1, num2)
num3 = int(input("Num3? = "))
print(z*num3)