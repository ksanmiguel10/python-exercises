# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name

# import functionsexercise
# print(functionsexercise.remove_vowels('something'))

# from functionsexercise import handle_commas
# print(handle_commas('234,567,889'))

# from functionsexercise import get_letter_grade as grade 
# print(grade(85))

# 2. For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# import itertools
# method1 = itertools.product('abc','123', repeat=1)
# print(list(method1))

# method2 = itertools.permutations('abc123', 2)
# print(list(method2))

# method3 = itertools.combinations('abc123', 2)
# print(list(method3))

# How many different ways can you combine two of the letters from "abcd"?
# method1 = itertools.product('abcd', repeat=2)
# print(list(method1))

# method2 = itertools.permutations('abcd', 2)
# print(list(method2))

# method3 = itertools.combinations('abcd', 2)
# print(list(method3))

# 3. Save this file as profiles.json. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json
data = json.load(open('profiles.json'))

# Total number of users
for key in data:
   tot_users = int((len(data)))
# print(tot_users)

# Number of active users
# for user in data:
#     if user['isActive'] == True:
#         print((len(user)))

# active_users = [user for user in data if user['isActive']]
# total_active = (len(active_users))
# print(total_active)

# Number of inactive users
# print(tot_users - total_active)

# Grand total of balances for all users
def bal_new(amt):
    amt = amt[1:] 
    amt = amt.replace(',', '') 
    return float(amt)

balances = [bal_new(user['balance']) for user in data]
# print(f'The total balance is $',sum(balances))
    
# Average balance per user
avg_bal = sum(balances) / len(balances)
print(avg_bal)


# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users