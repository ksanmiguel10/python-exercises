# Numpy Exercises
#Use the following code for the questions below:
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

negatives = [n for n in a if n < 0]

print(len(negatives))

# How many positive numbers are there?
positives = [n for n in a if n > 0]

print(len(positives))

# How many even positive numbers are there?

even_positives = [n for n in a if n > 0 and n % 2 == 0]

print(len(even_positives))

# If you were to add 3 to each data point, how many positive numbers would there be? 

new_array = a + 3
new_array

new_array_positives = [n for n in new_array if n > 0]
print(len(new_array_positives))

# If you squared each number, what would the new mean and standard deviation be?

a_squared = a ** 2
a_squared

print(a_squared.mean())

print(a_squared.std())

# A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

a.mean()

centered_data = a - a.mean()
print(centered_data)

# Calculate the z-score for each data point. Recall that the z-score is given by:
# Z=x−μ/σ

z_score_array = (a - a.mean()) / a.std()
print(z_score_array)

# Copy the setup and exercise directions from More Numpy Practice into your 4.7_numpy_exercises.py and add your solutions.
# More numpy practice

import numpy as np
# Life w/o numpy to life with numpy

# Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

# b = np.array(a)
# sum_of_a = b.sum()
# print(sum_of_a)

sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

# min_of_a = b.min()
# print(min_of_a)

min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

# max_of_a = b.max()
# print(max_of_a)

max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

# mean_of_a = b.mean()
# print(mean_of_a)

mean_of_a = sum_of_a / len(a)
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# product_of_a = b.prod()
# print(product_of_a)

import functools as f
product_of_a = f.reduce(lambda a, b: a * b, a)
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# squares_of_a = b ** 2
# print(squares_of_a)

squares_of_a = [n ** 2 for n in a]
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [n for n in a if n % 2 != 0]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [n for n in a if n % 2 == 0]
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

b2 = np.array(b)

# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
    
# print(sum_of_b)

sum_of_b = b2.sum()
print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = b2.min()

print(min_of_b)

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b2.max()
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = b2.mean()
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = b2.prod()
print(product_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = [n ** 2 for n in b2]
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = b2[(b2 % 2) != 0]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = b2[(b2 % 2) == 0]
print(evens_in_b)

# Exercise 9 - print out the shape of the array b.

print(b2.shape)

# Exercise 10 - transpose the array b.

print(np.transpose(b2))

#Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

print(np.reshape(b2, 6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

print(np.reshape(b2, (6, 1)))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c2 = np.array(c)

print(c2.min())
print(c2.max())
print(c2.sum())
print(c2.prod())

# Exercise 2 - Determine the standard deviation of c.

print(c2.std())

# Exercise 3 - Determine the variance of c.

print(np.var(c2))

# Exercise 4 - Print out the shape of the array c

print(c2.shape)

# Exercise 5 - Transpose c and print out transposed result.
c_trans = np.transpose(c2)
print(np.transpose(c2))

# Exercise 6 - Multiply c by the c-Transposed and print the result.

mult_c = (c2 * c_trans)
print(c2 * c_trans)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

print(mult_c.sum())

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


print(mult_c.prod())

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

d2 = np.array(d)

print(np.sin(d2))

# Exercise 2 - Find the cosine of all the numbers in d

print(np.cos(d2))

# Exercise 3 - Find the tangent of all the numbers in d

print(np.tan(d2))

# Exercise 4 - Find all the negative numbers in d

negative_in_d = d2[(d2 < 0)]
print(negative_in_d)

# Exercise 5 - Find all the positive numbers in d

positive_in_d = d2[(d2 > 0)]
print(positive_in_d)

# Exercise 6 - Return an array of only the unique numbers in d.

unique_d = np.unique(d2)
print(np.unique(d2))

# Exercise 7 - Determine how many unique numbers there are in d.

print(len(unique_d))

# Exercise 8 - Print out the shape of d.

print(d2.shape)

# Exercise 9 - Transpose and then print out the shape of d.
trans_d = np.transpose(d2)
print(trans_d.shape)

# Exercise 10 - Reshape d into an array of 9 x 2

print(np.reshape(d2, (9, 2)))
