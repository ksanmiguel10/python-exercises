# # 1a
# # Conditional Basics
# # prompt the user for a day of the week, print out whether the day is Monday or not
# weekday = input('Please enter a weekday: ')
# print(f'weekday = {weekday}')
# if weekday == 'Monday':
#     print("It's Monday!")
# else:
#      print('It is not Monday')

# # 1b prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# weekday = input('Please enter a day of the week: ')
# if weekday == 'Saturday' or weekday == 'Sunday':
#     print('It is a weekend')
# else:
#     print('It is a weekday')

# # 1c create variables and make up values for the number of hours worked in one week the hourly rate how much the week's paycheck will be. write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
# hours_worked = 50
# hourly_rate = 22
# if hours_worked > 40:
#     regular_rate = 40 * hourly_rate
#     overtime_pay = (hours_worked - 40) * hourly_rate * 1.5
#     paycheck = regular_rate + overtime_pay
# else:
#     paycheck = hourly_rate * hours_worked
# print(paycheck)


# # Loop Basics
# # 2a While Loops
# # Create an integer variable i with a value of 5.
# i = int(5)

# # Create a while loop that runs so long as i is less than or equal to 15
# # Each loop iteration, output the current value of i, then increment i by one.
# # Your output should look like this:
# # 5 6 7 8 9 10 11 12 13 14 15
# while i <= 15:
#     print(i)
#     i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# counter = 0
# while counter <= 100:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1

# Alter your loop to count backwards by 5's from 100 to -10.
# counter = 100
# while counter <= 100:
#     if counter in range(-10,101):
#         print(counter)
#     counter -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# 2 4 16 256 65536
# x = 2
# while x < 1_000_000:
#     print(x)
#     x = x * x

# Write a loop that uses print to create the output shown below.
# counter = 100
# while counter <= 100:
#     if counter in range(5,101):
#         print(counter)
#     counter -= 5

# 2b For Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# For example, if the user enters 7, your program should output:
# n = input('Give me a number: ')
# n_int=int(n)
# i = 1
# for numbers in n:
#     while i <= 10:
#         print(n, 'x', i, '=', (n_int*i))
#         i += 1

# Create a for loop that uses print to create the output shown below.
# count = 1
# for n in range(count):
#     while count <=9:
#         print(f'{str(count)*count}')
#         count +=1

# 2c break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# user_number = input('Give me an odd number between 1 and 50: ')
# while not user_number.isdigit():
#     user_num = input('Give me a valid odd number between 1 and 50: ')
#     if user_num.isdigit() and int(user_num) % 2 != 0 and int(user_num) < 50 and int(user_num) > 0:
#         break

# print(f'Number to skip is: {user_num} \n \n')
# for n in range(1,51):
#     if n == int(user_num):
#         print(f'Yikes! Skipping number: {user_num}')
#         continue
#     else:
#         if n % 2 != 0 and n != user_num:
#             print(f'Here is an odd number: {n}')
#             n += 1

# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
# user_pos = input('Please input a positive number: ')
# while not user_pos.isdigit():
#     user_pos = input('Please input a valid positive number: ')
#     if user_pos.isdigit() and int(user_pos) > 0 :
#         break

# for n in range(int(user_pos) + 1):
#     print(n)

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
# user_pos = input('Please input a positive integer: ')
# while not user_pos.isdigit():
#     user_pos = input('Please input a valid positive integer: ')
#     if user_pos.isdigit() and int(user_pos) > 0 :
#         break

# user_pos = int(user_pos)
# while user_pos >= 1:
#     print(user_pos)
#     user_pos -= 1

# 3 Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# for n in range(0,101):
#     if n % 3 == 0 and n % 5 == 0:
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print('Fizz')
#     elif n % 5 == 0:
#         print('Buzz')
#     else:
#         print(n)

# 4 Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# user_input = input('What number would you like to go up to?')
# while not user_input.isdigit():
#     user_input = input('What number would you like to go up to? ')
#     if user_input.isdigit() and int(user_input) > 0 :
#         break
# user_input = int(user_input)
# print('number | squared | cubed')
# print('------------------------')
# for n in range(1,user_input + 1):
#     print(f'{n}      | {n*n}     | {n*n*n}')

# Bonus: Research python's format string specifiers to align the table

# 5 Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# while True:
#     grade = input('Please input a grade from 0 to 100: ')
#     if grade.isdigit() and int(grade) > 0 and int(grade) <= 100:
#         grade = int(grade)
#         if grade >= 88 and grade <= 100: print('A')
#         if grade >= 80 and grade <= 87: print('B')
#         if grade >= 67 and grade <= 79: print('C')
#         if grade >= 60 and grade <= 66: print('D')
#         if grade <= 59: print('F')
#         exit = input('Do you want to exit?')
#         if exit.lower() == 'yes' or exit.lower() == 'y':
#             break
#         elif exit.lower() == 'no' or exit.lower() == 'n':
#             continue

# 6 Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
# books = [{"title":"Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "genre":"Fantasy"}]
# books.append({"title":'The Hunger Games', "author":'Suzanne Collins', 'genre':'Science Fiction'})
# books.append({"title":"To All the Boys I've Loved Before", 'author':'Jenny Han', 'genre':'Romance'})


# genre = input("What Genre would you like?")
# print(f"Books with the genre: {genre}")
# for i in books:
#     if i['genre'].lower() == genre.lower():
#         print(i['title'])
