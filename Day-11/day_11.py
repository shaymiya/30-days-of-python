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
        
slope = calculate_slope()

if slope:
    print('=====================\nThe slope is:', slope)

print('-----------------------------------')
