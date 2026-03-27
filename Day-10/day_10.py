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

# Reverse the fruit list order using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
for index in range(len(fruits) - 1, -1, -1):
    print(fruits[index])

print('----------------------------')

# Use the countries_data.py file and do the following operations

from countries_data import countries_data

# What are the total number of languages in data?
languages = list() # create an empty list for all the languages

for country in countries_data: # iterate through countries
    for language in country.get('languages'): # iterate through languages
        # if there is a new language, add the language in the languages list
        if language not in languages:
            languages.append(language)
            print(f'A new language "{language}" added')

print(len(languages))

print('----------------------------')

# Find the ten most spoken languages from the data
most_spoken_languages = {} #create an empty dictionary for storing the # of speakers

# iterate through countries
for country in countries_data:
    # iterate through languages
    for language in country.get('languages'):
        # if language does not exist in the dictionary, add it to the dictionary with value of 1
        if language not in most_spoken_languages:
            most_spoken_languages[language] = 1
            print('New language added to the dictionary: ', language)
        else:
            # if language exists in the dictionary, add +1 to the value
            most_spoken_languages[language] += 1
            print('Language updated: ', language)

# for language, value in most_spoken_languages.items():
#     print(language, value)

# how to organize the dictionary?

# we can get the max value out of the dictionary
print('Top speakers: ', max(most_spoken_languages.values()))

# copy dictionary into top ten languages
top_ten_languages = most_spoken_languages.copy()

# run the loop 10 times
for i in range(1,11):
    for language, value in top_ten_languages.items(): # loop through the languages
        if value == max(top_ten_languages.values()): # find the max value
            print(i, language, value) # print it out
            top_ten_languages[language] = 0 # set the max value to 0
            break # break out the loop and find the next max value

print('----------------------------')

# Find the 10 most populated countries in the world
most_populated_countries = {}

for country in countries_data:
    most_populated_countries[country.get('name')] = country.get('population')

for i in range(1,11):
    for name, population in most_populated_countries.items():
        if population == max(most_populated_countries.values()):
            print(i, name, population)
            most_populated_countries[name] = 0
            break

print('----------------------------')
