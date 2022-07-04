# y = int(input('Enter number of rows required: '))
# for x in range(y):
#     for u in range(-6,-x):
#         print(" ", end='')
# for s in range(x+1):
#     print('* ', end='')
# print()

for i in range(y, 0, -1):
    for j in range(y - i):
        print(' ', end='')

    for k in range(i):
        print('* ', end='')
    print()


