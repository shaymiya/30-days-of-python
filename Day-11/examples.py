# DAY 11 - FUNCTIONS
# So far we have seen many built-in Python functions. In this section, we will focus
# on custom functions. Before we start making functions let's learn what a function is
# and why do we need them:
# 
# DEFINING A FUNCTION
# A function is a REUSABLE BLOCK OF CODE or programming statements designed to perform
# a certain task. To define or declare a function, Python provides the DEF keyword.
# 
# DECLARING AND CALLING A FUNCTION
# When we make a function, we call it DECLARING a function. When we start to use it,
# we call it CALLING or invoking a function. Functions can be declared with or without
# parameters.

# Declaring the generate full name function
def generate_full_name ():
    first_name = 'Shay'
    last_name = 'Miya'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

# Calling the function
generate_full_name()

# Declaring another function
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()

# FUNCTION RETURNING A VALUE - PART 1
# Functions return values using the return statement. If a function has no return
# statement, it returns None. Let's rewrite the above functions using return.
# From now on, we get a value from a function when we call the function and print it.

def generate_full_name():
    first_name = 'Shay'
    last_name = 'Miya'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())    

print('------------------------------')

# FUNCTION WITH PARAMETERS
# In a function we can pass different data types(number, string, boolean, list, tuple,
# dictionary or set) as parameters

# Single Parameter: If our function takes a parameter, we should call our function
#   with an argument

# Declaring a function
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Shay'))

def add_ten(num):
    ten = 10
    return num + ten

print('Add ten: ', add_ten(90))

def square_number(x):
    return x * x

print('Square number: ', square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area

print('Area of circle: ', area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print('Sum of numbers (10): ', sum_of_numbers(10))
print('Sum of numbers (100): ', sum_of_numbers(100))

print('------------------------------')

# Two Parameters: A function can have multiple parameters. If our function takes
#   parameters, we should call it with arguments. Let's test it with 2 parameters
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full name: ', generate_full_name('Shay', 'Miya'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2026, 2023))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity) + ' N' # to display correctly, the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

print('------------------------------')

# PASSING ARGUMENTS WITH KEY AND VALUE
# If we pass the arguments with the KEY and VALUE, the order of arguments doesn't matter
print(generate_full_name(last_name = 'Miya', first_name = 'Shay'))
print(weight_of_object(gravity = 9.81, mass = 30))

print('------------------------------')

# FUNCTION RETURNING A VALUE - PART 2
# If we do not return a value with a function, then our function is returning None
# BY DEFAULT. To return a value with a function we use the keyword return followed
# by the variable we are returning. We can return any kind of data types from a function:

# Returning a string: Example
def print_full_name(first_name, last_name):
    return first_name + ' ' + last_name
print('Full name: ', print_full_name('Shay', 'Miya'))

# Returning a number: Example
print('Age: ', calculate_age(2026, 2022))

# Returning a boolean: Example
def is_even (n):
    if n % 2 == 0:
        return True # NOTE! Return stops further execution of the function!
    return False

print(is_even(3))
print(is_even(10))

print('------------------------------')

# Returning a list: Example
def find_even_numbers (n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

print('------------------------------')

# FUNCTION WITH DEFAULT PARAMETERS
# Sometimes we pass default values to parameters when we invoke the function. If we
# do not pass arguments when calling the function, their default values will be used

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Shay'))

def calculate_age (birth_year, current_year = 2026):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2022))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity) + ' N'
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # average gravity on Earth
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the Moon

print('------------------------------')

# ARBITARY NUMBER OF ARGUMENTS
# IF we do not know the number of arguments we pass to our function, we can create a
# function which can take ARBITATY NUMBER OF ARGUMENTS by adding * before the parameter name!
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,3,4,6,1))

print('------------------------------')

# DEFAULT AND ARBITARY NUMBER OF PARAMETERS IN FUNCTIONS
def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1', 'Shay', 'Theus', 'Nax', 'Crow')

print('------------------------------')

# DICTIONARY UNPACKING
# You can call a function which has named arguments using a dictionary with matching
# key names. You do so using **

# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print('Hi there', name, 'how is the weather in', location)

# Call the function using keyword arguments
greet(name = 'Alice', location = 'New York')

# Create a dictionary with keys matching the functions parameter names
my_dict = {'name': 'Alice', 'location': 'New York'}

# Call the function using dictionary unpacking
greet(**my_dict)
# The ** operator unpacks the dictionary, passing its key-value pairs
# as keyword arguments to the function.

print('------------------------------')

# ARBITARY NUMBER OF NAMED ARGUMENTS
# You can also define a function to accept an arbitary number of named arguments
def arbitary_named_args(**args):
    print('I received an arbitary number of arguments, totaling', len(args))
    print('They are provided as a dictionary in my function:', type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(' * key:', k, 'value:', v)

print(arbitary_named_args(**my_dict))

# Generally avoid this unless required as it makes it harder to understand what 
# the function accepts and does

print('------------------------------')

# FUNCTION AS A PARAMETER OF ANOTHER FUNCTION
# You can pass functions around as parameters
def square_number(n):
    return n ** n
def do_something(f, x):
    return f(x) # f = function, needs to have () right after!
print(do_something(square_number, 3))

print('------------------------------')
