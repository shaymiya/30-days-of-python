# Day 2: 30 Days of Python Programming

import math

# EXERCISES : LVL 1
first_name = 'Shay'
last_name = 'Miya'
full_name = f'{first_name} {last_name}'
country = 'Finland'
city = 'ToyShelf'
age = 3
year = 2026
is_married = False
is_true = True
is_light_on = True
is_hungry, is_thirsty, wants_coffee, loves_mama, mamas_age, mamas_name = False, True, True, True, 33, 'Cofi'

exercise_1_variables = [
    first_name,
    last_name,
    full_name,
    country,
    city,
    age,
    year,
    is_married,
    is_true,
    is_light_on,
    is_hungry,
    is_thirsty,
    wants_coffee,
    loves_mama,
    mamas_age,
    mamas_name
]


# EXERCISES : LVL 2

# use for loop for checking the types of all previous variables
for item in exercise_1_variables:
    print(f'Type:{type(item)} -> {item}')

# find the length of the first name
print(len(first_name))

# compare the length of the first and last name
print(min([len(first_name), len(last_name)]))

# declare some numbers and do stuff with them
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# The radius of circle is 30 meters
radius = 30.0
area_of_circle = math.pi * radius**2
print(f'Area of a circle with 30m radius is about {round(area_of_circle)} m^2')
circum_of_circle = (radius * 2) * math.pi
print(f'Circumfence of a cirle with 30m radius is about {round(circum_of_circle)}m')

def circle_area_calculator(radius):
    return math.pi * float(radius)**2

# Calculate the area of a custom circle with user input
user_radius = input('Set radius of the circle: ')
print(f'Area of a circle with {user_radius}m radius is about {round(circle_area_calculator(user_radius))} m^2')

first_name = input('First Name: ')
last_name = input('Last Name: ')
country = input('Country: ')
age = input('Age: ')

print(f'Nice to meet you {first_name} {last_name} from {country}! It seems you were born in {2026 - int(age)}, nice!')