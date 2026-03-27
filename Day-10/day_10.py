# EXERCISES : DAY 10

# Exercises : Level 1
# Iterate 0 to 10 using for loop & while loop
for number in range(11):
    print(number)
else:
    print('Iterating 0 - 10 using for loop')

print('----------------------------')

number = 0
while number <= 10:
    print(number)
    number += 1
else:
    print('Iterating 0 - 10 using while loop')

print('----------------------------')

# Iterate 10 to 0 using for loop, do the same using while loop

for number in range(10,-1,-1):
    print(number)
else:
    print('Iterating 10 - 0 using for loop')

number = 10
while number >= 0:
    print(number)
    number -= 1
else:
    print('Iterating 10 - 0 using while loop')

print('----------------------------')

# Make a loop that makes seven calls to print() so we get a # triangle
for num in range(1,8):
    print(f'{'#' * num}')

print('----------------------------')

# Use nested loops to create a # rectangle
hash = ''
for num in range(8):
    for i in range(8):
        hash += '# '
    print(hash)
    hash = ''

print('----------------------------')

# Print a num x num = total from 0 - 10 using loops
for num in range(11):
    print(f'{num} x {num} = {num ** 2}')

print('----------------------------')

# Iterate through the given list using for loop and print out the items
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for language in lst:
    print(language)

print('----------------------------')

# Use for loop to iterate from 1 - 100 and print only even numbers
for i in range(1,101):
    if i % 2 == 0:
        print(i)

print('----------------------------')

# Use for loop to iterate from 1 - 100 and print only odd numbers
for i in range(1,101):
    if i % 2 == 0:
        continue
    print(i)

print('----------------------------')

# Exercises : Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers
total = 0
for i in range(101):
    total += i
else:
    print('The sum of all numbers is', total)

print('----------------------------')

# Use for loop to iterate from 0 - 100 and print the sum of all evens and all odds
evens = 0
odds = 0
for num in range(101):
    if num % 2 == 0:
        evens += num
    else:
        odds += num
else:
    print(f'The sum of all evens is {evens}. The sum of all odds is {odds}.')

print('----------------------------')

# Exercises : Level 3
# Go to the data folder and use the countries.py file. Loop through the countries
# and extract all the countries containing the word land:
import countries

for country in countries.countries:
    if country.find('land') != -1:
        print(country)

print('----------------------------')
