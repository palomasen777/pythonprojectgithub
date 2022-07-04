import math
n = int(input("Give me a number: "))
while n>1:
    m = n%10
    print(math.trunc(m))
    n = n/10

