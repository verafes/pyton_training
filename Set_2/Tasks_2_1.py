# Real code challenges. Set #2
# Completed_solutions 1-10

# Task 1. Convert boolean values to strings 'Yes' or 'No'.
https://www.codewars.com/kata/53369039d7ab3ac506000467
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"
	
# Task 2. Keep Hydrated!
https://www.codewars.com/kata/582cb0224e56e068d800003c
# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, 
# rounded to the smallest value.
# For example:
# time = 3 ----> litres = 1
# time = 6.7---> litres = 3
# time = 11.8--> litres = 5

def litres(time):
    return time // 2

# Task 3. How many times should I go?
https://www.codewars.com/kata/53369039d7ab3ac506000467
# Complete the method that takes a boolean value and return a "Yes" string for true, 
# or a "No" string for false.

def how_many_times(annual_price, individual_price):
    count = int(annual_price / individual_price)
    return count if annual_price % individual_price == 0 else count + 1

# Solution #2
https://www.codewars.com/kata/57efcb78e77282f4790003d8
# Lot of museum allow you to be a member, for a certain amount amount_by_year you can have unlimitted acces to the museum.
# In this kata you should complete a function in order to know after how many visit it will be better to take an annual pass. 
#  The function take 2 arguments annual_price and individual_price.

import math
def how_many_times(annual_price, individual_price):
    return math.ceil(annual_price/individual_price)
	
# Task 4. Number of Decimal Digits
https://www.codewars.com/kata/58fa273ca6d84c158e000052
# Determine the total number of digits in the integer (n>=0) given as input to the function. 
# For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. 
# Be careful to avoid overflows/underflows.

def digits(n):
    return len(str(n))

# Task 5. Basic Mathematical Operations
# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
# Examples
# basic_op('+', 4, 7)         # Output: 11
# basic_op('-', 15, 18)       # Output: -3
# basic_op('*', 5, 5)         # Output: 25
# basic_op('/', 49, 7)        # Output: 7

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return "Error"


# Task 6. Area of a Square
https://www.codewars.com/kata/5748838ce2fab90b86001b1a
#Complete the function that calculates the area of the red square, 
#when the length of the circular arc A is given as the input. 
#Return the result rounded to two decimals.

def square_area(A):
    from math import pi
    r = (A*4)/(2*pi)
    area = r**2
    return (round(area, 2))

# Task 7. Convert a Boolean to a String
https://www.codewars.com/kata/551b4501ac0447318f0009cd
# Implement a function which convert the given boolean value into its string representation.
def boolean_to_string(b):
    return str(b)
	
# Task 8. Hello, Name or World!
https://www.codewars.com/kata/57e3f79c9cb119374600046b
# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! 
# if name is not given (or passed as an empty String).
# Assuming that name is a String and it checks for user typos to return a name 
# with a first capital letter (Xxxx).
# Examples:
# hello "john"   => "Hello, John!"
# hello "aliCE"  => "Hello, Alice!"
# hello          => "Hello, World!" # name not given
# hello ''       => "Hello, World!" # name is an empty String

def hello(name=""):
    if name:
        return f"Hello, {name.title()}!"
    else:
         return f"Hello, World!"

# Task 9. Remove First and Last Character
https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
# It's pretty straightforward. Your goal is to create a function that removes 
# the first and last characters of a string. You're given one parameter, the original string. 
# You don't have to worry with strings with less than two characters.

def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]

# Task 10. Remove exclamation marks
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return s.replace("!","")

# 
