# DAY 13 - LIST COMPREHENSION
# List comprehension in Python is a compact way of creating a list from a sequence.
# It is a short way to create a new list. List comprehension is CONSIDERABLY FASTER
# than processing a list using the for loop!

# syntax:
# [expression for i in iterable if condition]

# For instance, if you want to change a string to a list of characters, you can use 
# a couple of methods:

# One way:
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

print('--------------------------------')

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))
print(lst)

print('--------------------------------')

# Example 2 : generating a list of numbers
numbers = [i for i in range(11)]    # to generate numbers from 0 to 10
print(numbers)

print('--------------------------------')

# It is possible to do a mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)

print('--------------------------------')

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)

print('--------------------------------')

# Example 3 : list comprehension can be combined with if expression
# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

print('--------------------------------')

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

print('--------------------------------')

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

print('--------------------------------')

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

print('--------------------------------')

# LAMBDA FUNCTION
# Lambda function is a small anonymous function without a name. It can take any number
# of arguments, but can only have one expression. Lambda function is similar to anonymous
# functions in JavaScript. We need it when we want to write an anonymous function inside
# another function!

# CREATING A LAMBDA FUNCTION
# To create a lambda function we use lambda keyword followed by parameter(s), followed
# by an expression. Lambda function does not use return but it explicitly returns THE
# EXPRESSION

# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(3, 4, 5))

print('--------------------------------')

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 4))

# Let's change the above function to a LAMBDA function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 4))

print('--------------------------------')

# SELF INVOKING lambda function
(lambda a, b: a + b)(2,3)           # 5 - need to encapsulate it in print() to see result
print((lambda a, b: a + b)(2,3))

print('--------------------------------')

square = lambda x : x ** 2
print(square(3))
cube = lambda x : x ** 3
print(cube(3))

print('--------------------------------')

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))

print('--------------------------------')

# LAMBDA FUNCTION INSIDE ANOTHER FUNCTION
# Using a lambda function inside another function
def power(x):
    return lambda n : x ** n

# Function power needs now 2 ARGUMENTS to run, in SEPARATE ROUNDED BRACKETS
cube = power(2)(3)
print(cube)

two_power_of_five = power(2)(5)
print(two_power_of_five)

print('--------------------------------')
