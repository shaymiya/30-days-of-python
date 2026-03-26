# EXERCISES : DAY 09

# Exercises : Level 1
# Get user input using input(). If user is 18 or older, give feedback: You are old enough to drive.
# If user is below 18 give feedback to wait for the missing amount of years.
user_age = int(input('Enter your age: '))
if user_age >= 18:
    print('You are old enough to drive!')
else:
    print(f'You need to wait only {18 - user_age} years to learn how to drive!')

print('----------------------------')

print('Who is older, me or you?')
my_age = 3
your_age = int(input('Enter your age: '))
age_gap = abs(your_age - my_age)

# check if user is more than 1 year older/younger
if age_gap == 1:
    year = 'year'
else:
    year = 'years'

# check if user is older or younger than me
if your_age > my_age:
    print(f'You are {age_gap} {year} older than me!')
elif your_age == my_age:
    print(f'Look at that, we are the same age!!')
else:
    print(f'You are {age_gap} {year} younger than me!')

print('----------------------------')

# compare 2 user submitted numbers
print('Let\'s compare some numbers!')
a = int(input('Number 1: '))
b = int(input('Number 2: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is less than {b}')
else:
    print(f'{a} is equal to {b}')

print('----------------------------')

# Exercises : Level 2 !

# Write a code that gives grade to students according to their scores
import random

points = random.randint(0,100)
print(f'You scored {points} points!')
print('Grading in progress...')

# if elif else for grades
if points > 0 and points < 60:
    print('Your grade is F, bummer.')
elif points < 70:
    print('Your grade is D, that\'s tough!')
elif points < 80:
    print('Your grade is C, getting there!')
elif points < 90:
    print('Your grade is B, good job!')
else:
    print('You got an A, congratz!')

print('----------------------------')

# ask user for a month and let them know which season it is: 
# Autumn, Winter, Spring or Summer
autumn = ('September', 'October', 'November', '9', '10', '11')
winter = ('December', 'January', 'February', '12', '1', '2')
spring = ('March', 'April', 'May', '3', '4', '5')
summer = ('June', 'July', 'August', '6', '7', '8')

current_month = input('What month it is? ').title()

if current_month in autumn: season = 'Autumn'
elif current_month in winter: season = 'Winter'
elif current_month in spring: season = 'Spring'
elif current_month in summer: season = 'Summer'
else: season = None

if not season:
    print('Hmmm.. That doesn\'t sound like a month to me')
else:
    print(f'Oh, so it is {season} already!')


print('----------------------------')

# if a fruit does not exist, add the fruit to the list and print the updated list
# if fruit exists, print That fruit already exists in the list
fruits = ['banana', 'orange', 'mango', 'lemon']

print('Welcome to the Fruit Basket!')
print('We have so many fruits here, look! ->', ', '.join(fruits).title())
new_fruit = input('What fruit would you like to add to the basket? ').lower()
if new_fruit in fruits:
    print('That fruit already exists in the basket!')
else:
    fruits.append(new_fruit)
    print('Thank you for adding your fruit to the basket!')
    print(f'Now we have {', '.join(fruits[:-2]).title()}, and {fruits[-1].title()} in the basket!')

print('----------------------------')

# EXERCISES : LEVEL 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

# check if the person dictionary has skills key, if so print out the middle skill in
# the skills list

if person.get('skills'):
    middle = int(len(person['skills']) / 2)
    print(f'{person['first_name']}\'s middle skill is: {person['skills'][middle]}')
    # if person knows python, print out the result
    if 'Python' in person['skills']:
        print(f'{person['first_name']} knows some Python, nice!')

if person.get('skills'):
    if 'JavaScript' and 'React' in person['skills'] and len(person['skills']) == 2:
        print('He is a front end developer')
    elif 'Node' and 'Python' and 'MongoDB' in person['skills'] and len(person['skills']) == 3:
        print('He is a backend developer')
    elif 'React' and 'Node' and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')

print('----------------------------')
