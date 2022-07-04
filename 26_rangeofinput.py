y = int(input('No. '))
m = False
for x in range(2, y):
    a = y % x
    if a == 0:
        m = True
        break

if m == True:
    print('It is not a prime number')
else:
    print('It is a prime number')

