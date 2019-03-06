# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
# def is_two(x):
#     if x == '2' or x == 2:
#         return True
#     else:
#         return False

# print(is_two(2))
# print(is_two('2'))
# print(is_two('5'))

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# def is_vowel(x):
#     if x.lower() == 'a' or x.lower() == 'e' or x.lower() == 'i' or x.lower() == 'o' or x.lower() == 'u':
#         return True
#     else:
#         return False

# print(is_vowel('a'))
# print(is_vowel('A'))
# print(is_vowel('m'))

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# def is_consonant(x):
#     if x.lower() == 'a' or x.lower() == 'e' or x.lower() == 'i' or x.lower() == 'o' or x.lower() == 'u':
#         return False
#     else:
#         return True

# print(is_consonant('e'))
# print(is_consonant('U'))
# print(is_consonant('T'))

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
# def capital_consonant(word):
#     if word[0] != 'a' and word[0] != 'e' and word[0] != 'i' and word[0] != 'o' and word[0] != 'u':
#         return ''.join(word[0].upper() + word[1:])
#     else:
#         return ''.join([word])

# print(capital_consonant('orange'))
# print(capital_consonant('something'))
# print(capital_consonant('green'))
# print(capital_consonant('elephant'))

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# def calculate_tip(percentage, bill_total):
#     percentage = percentage/100
#     bill_total = float(bill_total)
#     amt_to_tip = percentage * bill_total
#     return '{:,.2f}'.format(amt_to_tip) 

# print('Amount to tip is $',calculate_tip(18, 100))
# print('Amount to tip is $',calculate_tip(15, 23742))
# print('Amount to tip is $',calculate_tip(20, 467))

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
# def apply_discount(original_price, discount_percentage):
#     original_price = float(original_price)
#     discount_percentage = discount_percentage/100
#     new_price = original_price - (original_price * discount_percentage)
#     return '${:,.2f}'.format(new_price)

# print(apply_discount(49.99, 25,))

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# def handle_commas(str_number):
#     return int(str_number.replace(',', '')) 

# print(handle_commas('2,100,050'))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# def get_letter_grade(grade):
#     grade = int(grade)
#     if grade >= 88 and grade <= 100: return('A')
#     elif grade >= 80 and grade <= 87: return('B')
#     elif grade >= 67 and grade <= 79: return('C')
#     elif grade >= 60 and grade <= 66: return('D')
#     elif grade <= 59: return('F')

# print(get_letter_grade(85))
# print(get_letter_grade(45))
# print(get_letter_grade(90))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# def remove_vowels(text):
#     vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
#     for char in text:
#         if char in vowels:
#             text = text.replace(char, '')
#     return text
            
# print(remove_vowels('elephant'))
# print(remove_vowels('BEAUTIFUL'))
# print(remove_vowels('Computer'))

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
# def normalize_name(name):
#     return ((name.lower()).strip()).replace(' ', '_')

# print(normalize_name('   KATY SALTS '))
# print(normalize_name('   % Completed '))

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# sums = []
# def cumsum(numbers):
#     sums.append(numbers[0])
#     for i in range(len(numbers) - 1):
#         if i == 0:
#             sums.append(numbers[i] + numbers[i + 1])
#         else:
#             sums.append(numbers[i + 1] + sums[i])
#     return sums

# numbers = [1,1,1]
# numbers2 = [1,2,3,4]
# numbers3 = [4,8,10,25]
# numbers4 = [8,3,0,12,47]
# print(cumsum(numbers4))