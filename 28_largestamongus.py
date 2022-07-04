listOfNumbers = []

m = int(input("How many numbers would you like to put in: "))
for j in range(0, m):
    p = int(input("Enter number: "))
    listOfNumbers.append(p)

listOfNumbers.sort()
print(listOfNumbers[-1])




