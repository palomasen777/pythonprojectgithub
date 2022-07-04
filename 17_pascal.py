
n = int(input("Enter number of rows: "))

for i in range(n+1):
  for j in range(n-i):
     print(' ', end='')
  C = 1
  for j in range(1, i+1):
     print(C, ' ', end='')2
     C = C * (i - j) // j
  print()
