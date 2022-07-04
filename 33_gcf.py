no_one = int(input("1st Number: "))
no_two = int(input("2nd Number: "))
if no_one>no_two:
    s = no_two
else:
    s = no_one
for i in range(1, s+1):
    if no_one % i == 0 and no_two % i == 0:
        gcf = i
print(gcf)

