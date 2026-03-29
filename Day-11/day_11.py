# EXERCISES : DAY 11

# Exercises : Level 1

# Define a function that adds two numbers and returns a sum
def add_two_numbers(num_one, num_two):
    return num_one + num_two

print('Sum: ', add_two_numbers(2, 3))

# Define a function that calculates the area of a circle
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    print('Area of circle with radius of', r, 'is:', area)

area_of_circle(4)

# Write a function called add_all_nums which takes arbitary number of arguments
# and returns their sum. Check if all the list items are number types. If not, do
# give a reasonable feedback:
def add_all_nums(*nums):
    sum = 0
    # check if the num is digit, let user know if it isn't, and add only the numbers 
    for num in nums:
        try: sum += float(num)
        except ValueError: print(num, 'is not a number')
    return sum

print('Sum: ', add_all_nums(1, 2, 3, 4, 'test', 10, 3.4))

# Write a function that converts celcius to fahrenheit
def convert_celcius_to_fahrenheit(celsius):
    try: 
        float(celsius)
        print('Converting', celsius, 'Celsius to Fahrenheit')
        fahrenheit = (float(celsius) * 9 / 5)  + 32
        return fahrenheit
    except ValueError: 
        print(celsius, 'is not a number!')

print('Celsius to Fahrenheit:', convert_celcius_to_fahrenheit(24), 'F')

print('-----------------------------------')

# Write a function called check_season. It takes month as a parameter and returns the season:
# Autumn, Winter, Spring or Summer
def check_season(month):
    autumn = ('September', 9, 'October', 10, 'November', 11)
    winter = ('December', 12, 'January', 1, 'February', 2)
    spring = ('March', 3, 'April', 4, 'May', 5)
    summer = ('June', 6, 'July', 7, 'August', 8)

    if month in autumn:
        print(f'{month}? So it is Autumn already!')
    elif month in winter:
        print(f'{month}? So it is Winter already!')
    elif month in spring:
        print(f'{month}? So it is Spring already!')
    elif month in summer:
        print(f'{month}? So it is Summer already!')
    else:
        print(f'{month}..? Are you sure you typed that correctly?')

check_season('january'.title())

print('-----------------------------------')

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope():
    user_input = input('Is your equation in the following form: y = mx + b ? (y/n) > ').lower()
    if user_input == 'y':
        m = input('Please give the value of m in the equation y = mx + b > ')
        return m
    else:
        user_input = input('Is your equation in form of: Ax + By = C ? (y/n) > ').lower()
        if user_input == 'y':
            A = float(input('Please give the value of A in the equation: '))
            B = float(input('Please give the value of B in the equation: '))
            return -(A / B)
        else:
            user_input = input('Do you know 2 points (x, y) of the equation? (y/n) > ').lower()
            if user_input == 'y':
                print(f'(x1, y1) (x2, y2)')
                x1 = float(input('Please give the value of x1  > ').strip())
                print(f'({x1}, y1) (x2, y2)')
                y1 = float(input('Please give the value of y1 > ').strip())
                print(f'({x1}, {y1}) (x2, y2)')
                x2 = float(input('Please give the value of x2  > ').strip())
                print(f'({x1}, {y1}) ({x2}, y2)')
                y2 = float(input('Please give the value of y2 > ').strip())
                print(f'({x1}, {y1}) ({x2}, {y2})')
                 
                return ((y2 - y1) / (x2 - x1))
            else:
                print("I'm sorry, I can't help you with your equation")

# HOW TO MAKE THIS LOOK NEATER? ^ ;;
# Welp, at least it works . U . ;;;;

slope = calculate_slope()

if slope:
    print('=====================\nThe slope is:', slope)

print('-----------------------------------')

# Quadratic equation is calculated as follows: ax^2 + bx + c = 0
# Write a function which calculates solution set of a quadratic equation,
# solve_quadratic_eqn
def solve_quadratic_eqn(a, b, c):
    # print out the steps?
    print(f'{a}x^2 {'+' if b >= 0 else '-'} {abs(b)}x {'+' if c >= 0 else '-'} {abs(c)} = 0')
    print('Solving the equation....')
    print('Using the quadratic equation\'s formula:')
    print(f'                 _____________________')
    print(f'     -({b}) +/- v/({b})^2 - 4({a})({c})')
    print(f' x = ----------------------------------')
    print(f'                 2({a})')
    
    print(f'              ________')
    print(f'      {-b} +/- v/{b**2} - {4 * a * c}')
    print(f' x = --------------------')
    print(f'            {2 * a}')

    print(f'              ____')
    print(f'      {-b} +/- v/ {b**2 - 4 * a * c}')
    print(f' x = ---------------')
    print(f'          {2 * a}')

    print(f'\n       {-b} + {((b**2 - 4 * a * c)**0.5):.2f}           {-b} - {((b**2 - 4 * a * c)**0.5):.2f}')
    print(f' x = ------------   x = ------------')
    print(f'           {2 * a}                  {2 * a}')

    print(f'\n Roots: x = {((-b + (b**2 - 4 * a * c)**0.5) / 2 * a):.2f}  and  x = {((-b - (b**2 - 4 * a * c)**0.5) / 2 * a):.2f}')

solve_quadratic_eqn(2, -3, -4)

print('-----------------------------------')

# Declare a function named print_list. It takes list as a parameter and prints out 
# each element of the list
def print_list(list):
    for item in list:
        print('-', item.title())

fruits = ['banana', 'kiwi', 'avocado', 'apple']
print_list(fruits)

print('-----------------------------------')

# Declare a function named reverse_list. It takes an array as a parameter and it
# returns the reverse of the array (use loops)
def reverse_list(list):
    temp = []
    for index in range(len(list) - 1, -1, -1):
        temp.append(list[index])
    return temp

print(reverse_list(fruits))
print(reverse_list([1,2,3,4,5,6,7,8,9,10]))

print('-----------------------------------')

# Declare a function named capitalize_list_items. It takes a list as a parameter and 
# it returns a capitalized list of items
def capitalize_list_items(list):
    temp = []
    for item in list:
        temp.append(item.capitalize())
    return temp

print(capitalize_list_items(fruits))

print('-----------------------------------')

# Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
def add_item(list, item):
    list.append(item)
    return list

print(fruits)
print(add_item(fruits, 'orange'))
print(fruits)

print('-----------------------------------')

# Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it
def remove_item(list, item):
    if item in list: del list[list.index(item)]
    else: print('Item not found in a list')
    return list

print(remove_item(fruits, 'apple'))
print(remove_item(fruits, 'apple'))

print('-----------------------------------')

# Declare a function named sum_of_numbers. It takes number parameter and it adds
# all the numbers in that range
def sum_of_numbers(number):
    sum = 0
    for num in range(number + 1):
        sum += num
    return sum

print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) 
print(sum_of_numbers(100)) 

print('-----------------------------------')

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the
# odd numbers in that range
def sum_of_odds(number):
    sum = 0
    for num in range(number + 1):
        if num % 2 != 0:
            sum += num
    return sum

print('Sum of odds:', sum_of_odds(100))

# Declare a function named sum_of_evens. It takes a number parameter and it adds all the
# even numbers in that range

def sum_of_evens(number):
    sum = 0
    for num in range(number + 1):
        if num % 2 == 0:
            sum += num
    return sum

print('Sum of evens:', sum_of_evens(100))

print('-----------------------------------')

# EXERCISES : LEVEL 2

# Declare a function named evens_and_odds. It takes a positive integer as parameter and it
# counts number of evens and oddds in the number
def evens_and_odds(num):
    evens = 0
    odds = 0
    for n in range(num + 1):
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f'The number of odds are: {odds}\nThe number of evens are: {evens}'

print(evens_and_odds(100))

print('-----------------------------------')

# Call  your function factorial. It takes a whole number as a parameter and it returns
# a factorial of the number

# The factorial of a non-negative integer n is the product of all positive integers 
# less than or equal to n. (also if n = 0 -> n = 1)
def factorial(num):
    product = num if num >= 1 else 1
    for n in range(num - 1, 0, -1):
            product *= n
    return product

print('Factorial of 5 is', factorial(5))
print('Factorial of 0 is', factorial(0))

print('-----------------------------------')

# Call your function is_empty, it takes a parameter and checks if it is empty or not
def is_empty(param):
    if param == None or param == '' or param == 0:
        return True
    else:
        return False

empty_param = None

print('Is parameter empty?', is_empty(fruits))
print('Is parameter empty?', is_empty(empty_param))

print('-----------------------------------')

# Write different functions which take lists. They should calculate_mean, calculate_median,
# calculate_mode, calculate_range, calculate_variance and calculate_std (standard deviation)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 10]

# Calculate mean (average)
def calculate_mean(list): # mean = average of a dataset
    # let's presume that the lists consist of numbers
    # average = sum of objects / num of objects
    sum = 0
    for num in list:
        sum += num
    return sum / len(list)
print('List\'s mean is:', calculate_mean(numbers))

# Calculate median (the middle number of the list OR average of the two middle nms)
def calculate_median(list):
    if len(list) % 2 == 0:
        return list[int(len(list) / 2)] + list[int(len(list) / 2) + 1] / 2
    else:
        return list[int(len(list) / 2)]
print("List's median is:", calculate_median(numbers))

# Calculate mode: (the value that occurs most often, can have no value, one value or more than one value)
def calculate_mode(list):
    # let's create a dictionary and insert list items as keys and the occurrences as values
    mode_dict = {}
    for item in list:
        if mode_dict.get(item) == None:
            # print('Add new item to the dictionary')
            mode_dict[item] = 1
        else:
            # print('Item already exists in dictionary:', item)
            mode_dict[item] += 1

    # check if there is no mode in the list:
    if max(mode_dict.values()) == 1:
        return 'The list contains no mode'
    
    # make a list of top occurrences
    mode_list = []
    for k, v in mode_dict.items():
        if v == max(mode_dict.values()):
            mode_list.append(k)
    
    # check if there are more than 1 modes
    if len(mode_list) == 1:
        return f'The list contains following mode: {mode_list[0]}'
    else:
        return f'The list contains following modes: {mode_list}'

print(calculate_mode(numbers))
print(calculate_mode(fruits))

# Calculate range: (highest value - lowest value)
def calculate_range(list):
    return max(list) - min(list)
print("List's range:", calculate_range(numbers))

# Calculate variance: (sum of (n - mean)^2 of each data points / num of data points)
def calculate_variance(list):
    sum = 0
    mean = calculate_mean(list)
    for num in list:
        sum += (num - mean) ** 2
    return sum / len(list)
print("List's variance:", calculate_variance(numbers))

# Calculate standard deviation: (square root of the variance)
def calculate_std(list):
    return calculate_variance(list) ** (1/2)
print(f"List's standard deviation: {calculate_std(numbers):.2f}")

print('-----------------------------------')

# Write a function called greet which takes default argument, name. If no argument is
# supplied it should print 'Hello, Guest!', otherwise it should greet the person by name
def greet(name = 'Guest'):
    print(f'Hello, {name}!')

greet()
greet('Shay')

print('-----------------------------------')

# Create a function called show_args to take an arbitary number of named arguments and print
# their names and values
def show_args(**args):
    unpacked_str = 'Received: '
    for k, v in args.items():
        unpacked_str += k.strip('\'') + ': ' + str(v).strip('\'') + ', '
    return unpacked_str[:-2]

print(show_args(name="Alice", age=30, city="New York"))

print('-----------------------------------')

# EXERCISES : LEVEL 3

print('-----------------------------------')
