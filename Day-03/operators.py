age = 3
height = 100.0
complex_nbr = 1 + 1j

# # Calculate triangle area from user input
# user_base = float(input('Enter base: '))
# user_height = float(input('Enter height: '))
# triangle_area = 0.5 * user_base * user_height
# print(f'The area of the triangle is {triangle_area}')

# print('---------------------------------------')

# # Calculate the perimeter of user defined triangle
# side_a = int(input('Enter side a: '))
# side_b = int(input('Enter side b: '))
# side_c = int(input('Enter side c: '))
# print(f'The perimeter of the triangle is {side_a + side_b + side_c}')

# print('---------------------------------------')

# # Calculate the area and the perimeter of user defined rectangle
# length = int(input('Enter the length of the rectangle: '))
# width = int(input('Enter the width of the rectangle: '))
# print('Calculating the area...')
# rect_area = length * width
# print(f'The area of the rectangle is {rect_area}')
# print('Calculating the perimeter...')
# rect_perimeter = 2 * (length + width)
# print(f'The perimeter of the rectangle is {rect_perimeter}')

# print('---------------------------------------')

# # Calculate the area and the perimeter of user defined circle
# pi = 3.14
# radius = float(input('Enter the radius of a circle: '))

# print('Calculating the area of the circle...')
# circ_area = pi * radius * radius
# print(f'The area of the circle is {circ_area}')

# print('Calculating the circumference of the circle...')
# circ_circumference = 2 * pi * radius
# print(f'The circumference of the cirle is {circ_circumference}')

# Calculate the slope, x-intercept and y-intercept of y = 2x - 2 | y = mx + b
# start by finding 2 points on the graph
def find_y(_x):
    return 2*_x - 2

def find_x(_y):
    return _y / 2 + 1

def find_slope(x1, x2):
    slope = (find_y(x2) - find_y(x1)) / (x2 - x1)
    print(f'Slope: {slope}')
    return slope

# x1 = int(input('Enter the x1: '))
# x2 = int(input('Enter the x2: '))

# find_slope(x1, x2)
# print(f'y-intercept of y = 2x - 2 is (0, {find_y(0)})')
# print(f'x-intercept of y = 2x - 2 is ({int(find_x(0))}, 0)')

# print('---------------------------------------')

# Find slope & euclidean distance between point (2, 2) and point (6, 10)
def euclidean_distance(x1, y1, x2, y2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance

# print(f'The slope between points (2,2) and (6,10) is {find_slope(2, 6)}')
# print(f'The euclidean distance between points (2,2) and (6,10) is {euclidean_distance(2,2,6,10)}')

# slope_1 = find_slope(x1, x2)
# slope_2 = find_slope(2, 6)

# print(f'Slope 1: {slope_1}')
# print(f'Slope 2: {slope_2}')

# if slope_1 > slope_2:
#     print('Slope 1 is steeper than slope 2')
# elif slope_1 == slope_2:
#     print('Slopes are identical')
# else:
#     print('Slope 2 is steeper than slope 1')

def find_y_second_degree(_x):
    y = _x ** 2 + 6 * _x + 9
    print(f'When x = {_x}, y = {y}')
    return y

# while True:
#     print('Find y = 0 in y = x^2 + 6x + 9')
#     user_x = float(input('Give x a value: '))
#     if find_y_second_degree(user_x) == 0.0:
#         print('You found the correct value!')
#         break
#     else:
#         user_input = input('Do you want to continue? (y/n): ').lower()
#         if user_input == 'n':
#             break

# # Find the length of 'python' and 'dragon' and make a falsy comparison statement
# print('Is python longer than dragon?', len('python') < len('dragon'))

# # Use and operator to check if 'on' is found in both 'python' and 'dragon'
# print('Is "on" found in both "python" and "dragon"?', 'on' in 'python' and 'on' in 'dragon')

# # Use in operator to check if jargon is in the sentence
# sentence = 'I hope this course is not full on jargon.'
# print(sentence, 'jargon' in sentence)

# print('There is no "on" in both dragon and python.', 'on' not in 'python' and 'on' not in 'dragon')

# # Find the length of the text python
# print(str(float(len('python'))))

# # Check if user's number is even
# user_num = int(input('Pick a number: '))

# if user_num % 2 == 0:
#     print('Your number is even')
# else:
#     print('Your number is odd')

# print('Are the values equal?', 7 // 3 == int(2.7))

# print('Are the types equal?', type('10') == type(10))

# print('Is int("9.8") equal to 10?', int(float('9.8')) == 10)

# # Calculate pay of the person
# hours = int(input('Enter hours: '))
# rate_per_hour = int(input('Enter rate per hour: '))
# print(f'Your weekly earning is {hours * rate_per_hour}')

# # Calculate the number of seconds the person have lived (max years = 100)
# while True:
#     years = int(input('Enter number of years you have lived: '))
#     if years > 100:
#         print(f'{years}? Are you sure about that? Let\'s try this again!')
#         continue
#     else:
#         days = years * 365
#         hours = days * 24
#         minutes = hours * 60
#         seconds = minutes * 60
#         print(f'You have lived for {seconds} seconds, that\'s a lot!')
#         break

exponents = [1, 2, 3, 4, 5]

for exponent in exponents:
    print(exponent, exponent ** 0, exponent ** 1, exponent ** 2, exponent ** 3)

