import math

glist = []
def tot(m):
    while m > 1:
        n = m % 10
        l = math.trunc(n)
        glist.append(l)
        print(l)
        m = m / 10

def showglist():
    for o in range(len(glist)):
        print(glist[o], end='')

q = int(input("Enter number: "))

tot(q)

showglist()
