# #triangle area
# def areaofTriangle(x, y):
#     print(0.5 * x * y)
#
# height = int(input("Enter height of your triangle: "))
# base = int(input("Enter base of your triangle: "))
# areaofTriangle(height, base)
#
# #rectangle area
# def areaofRectangle(x,y):
#     print(x * y)
#
# width = int(input("Enter the width of your rectangle: "))
# length = int(input("Enter the length of you rectangle: "))
# areaofRectangle(width, length)
#
# #circle
# def areaofCircle(x):
#     print(3.14 * x * x)
#
# radius = int(input("Enter the radius of your circle: "))
# areaofCircle(radius)
#
# #rhombus
#
# def areaofRhombus(x, y):
#     print(0.5 * x * y)
#
# length = int(input("Enter the length of your rhombus: "))
# height = int(input("Enter the length of your rhombus: "))
# areaofRhombus(length, height)
#
# #parrallelogram
# def areaofParallelogram(b, h):
#     print(b * h)
#
# base = int(input("Enter the base of your parallelgram: "))
# height = int(input("Enter the height of your parrallelogram: "))
# areaofParallelogram(base, height)

#trapezium
def areaofTrapezium(x, y, h):
    print(0.5 * h * (x+y))

lengtha = int(input("Enter length A of your trapezium: "))
lengthb = int(input("Enter length B of your trapezium: "))
height = int(input("Enter height of your trapezium: "))
areaofTrapezium(lengtha, lengthb, height)