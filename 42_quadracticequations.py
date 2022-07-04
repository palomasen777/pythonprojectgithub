# import matplotlib.pyplot
# def quadFunction(a,b,c):
#     print("First value of x =", -b+(b^2 - 4 * a * c)/2 * a)
#     print("Second value of x =", -b-(b^2 - 4 * a * c)/2 * a)
#
# a = int(input("Enter the 'a' value of your quadractic equation: "))
# b = int(input("Enter the 'b' value of your quadractic equation: "))
# c = int(input("Enter the 'c' value of your quadractic equation: "))
# quadFunction(a, b, c)

# importing required modules
import matplotlib.pyplot as plt
import numpy as np


# function to generate coordinates
# def create_plot(ptype):
#     # setting the x-axis values
#     x = np.arange(-10, 10, 0.01)
#
#     # setting the y-axis values
#     if ptype == 'linear':
#         y = x
#     elif ptype == 'quadratic':
#         y = x ** 2
#     elif ptype == 'cubic':
#         y = x ** 3
#     elif ptype == 'quartic':
#         y = x ** 4
#
#     return (x, y)
#
#
# # setting a style to use
# plt.style.use('fivethirtyeight')
#
# # create a figure
# fig = plt.figure()
#
# # define sub
# # define subplots and their positions in figure
# plt1 = fig.add_subplot(221)
# plt2 = fig.add_subplot(222)
# plt3 = fig.add_subplot(223)
# plt4 = fig.add_subplot(224)
#
# # plotting points on each subplot
# x, y = create_plot('linear')
# plt1.plot(x, y, color='r')
# plt1.set_title('$y_1 = x$')
#
# x, y = create_plot('quadratic')
# plt2.plot(x, y, color='b')
# plt2.set_title('$y_2 = x^2$')
#
# x, y = create_plot('cubic')
# plt3.plot(x, y, color='g')
# plt3.set_title('$y_3 = x^3$')
#
# x, y = create_plot('quartic')
# plt4.pl


# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1, 2, 3]
# corresponding y axis values
y = [2, 4, 1]

x1 = [1, 2, 3]
y1 = [4, 1, 3]

# plotting the points
plt.plot(x, y)
plt.plot(x1, y1)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
