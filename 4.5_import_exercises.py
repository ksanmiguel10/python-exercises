# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name

import functionsexercise
print(functionsexercise.remove_vowels('something'))

from functionsexercise import handle_commas
print(handle_commas('234,567,889'))

from functionsexercise import get_letter_grade as grade 
print(grade(85))

# 2. For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different ways can you combine two of the letters from "abcd"?