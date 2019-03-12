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





