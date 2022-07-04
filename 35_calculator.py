def addition():
    x = int(input("num1 = "))
    y = int(input("num2 = "))
    print(x + y)


def subraction():
    x = int(input("num1 = "))
    y = int(input("num2 = "))
    print(x - y)


def multiplication():
    x = int(input("num1 = "))
    y = int(input("num2 = "))
    print(x * y)


def division():
    x = int(input("num1 = "))
    y = int(input("num2 = "))
    print(x / y)


def percentage():
    x = int(input("num1 = "))
    y = int(input("num2 = "))
    j = x / y
    print(j * 100)


def exponents():
    x = int(input("num1 = "))
    y = int(input("num2 = "))
    print(x ** y)


while True:
    o = input("What operation do you want to do-Add , Subract, Multiply, Divide, Percentage of a number, Exponent: ")
    if o == "Add" or o == 'add':
        addition()
        break
    elif o == "Subtract" or o =="subtract":
        subraction()
        break
    elif o == "Multiply" or o == "multiply":
        multiplication()
        break
    elif o == "Divide" or o == "divide":
        division()
        break
    elif o == "percentage" or o =="Percentage":
        percentage()
        break
    elif o == "exponents" or o == "Exponents":
        exponents()
        break
    else:
        print("Invalid Input - TRY ASIAN")
