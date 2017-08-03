import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
from sklearn import tree
import tensorflow as tf


# collect string / test length

x = input("please enter input string:")

if len(x) < 8:
	print("your string is too start.")
	print("please enter a string with at least 6 characters.")


# prompt user to enter number / test if even or odd

y = input("please enter an integer:")
number = int(y)

if number % 2 == 0:
	print("your number is even.")
else:
	print("your number is odd.")


# Scalene triangle: All sides have different length
# Isosceles triangle: Two sides have the same length
# Equilateral triangle: All sides are equal

a = int(input("The length of side a ="))
b = int(input("The length of side b ="))
c = int(input("The length of side c ="))

if a != b and b != c and a != c:
	print("this is a scalene triangle.")
elif a == b and b == c and a == c:
	print("This is an equilateral triangle.")
else:
	print("This is an isosceles triangle.")

#Function
 def function(x):
    Y = x*x
    return Y

Z = function(10)

print (Z)

