n = 1
f = int(input("Enter number of rows: "))
for p in range(f):
    for j in range(p+1):
        print(n, end=" ")
        n = n+1
    print()
