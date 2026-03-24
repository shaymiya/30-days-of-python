# STRINGS IN PYTHON
# multiline string : ''' ''' or """ """
multiline_string  = '''I am a student and enjoy
learning about all the different things!'''
print(multiline_string)

# String concatenation = connecting strings together
first_name = 'Shay'
last_name = 'Miya'
space = ' '
full_name = first_name + space + last_name
print(full_name)

# Escape sequences in strings (\ followed by a character)
#   - \n: new line
#   - \t: tab (4 spaces)
#   - \\: back slash
#   - \': single quote
#   - \": double quote

print('I hope everyone is enjoying the Python Challenge. \nAre you ?') # line break

print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')

print('This is a backslash symbol (\\)')
print("In every programming language it starts with \"Hello World\"")

# STRING FORMATTING
# Old style formatting (% operator)
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floats
# "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
first_name = 'Shay'
last_name = 'Miya'
language = 'Python'
formated_string = 'I am %s %s. I\'m learning %s' %(first_name, last_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f' %(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' %(python_libraries)
print(formated_string)

print('-------------------------------------')

# New Style String Formatting (str.format) <- python v3
first_name = 'Shay'
last_name = 'Miya'
language = 'Python'
formated_string = 'I am {} {}. I\'m learning {}'.format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # {:.2f} limits it to 2 digits after decimal!
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius {} is {:.2f}'.format(radius, area)
print(formated_string)

print('-------------------------------------')

# STRING INTERPOLATION / f-STRINGS (python 3.6+)

a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}') # :.2f still limits the digits with f-strings!
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

print('-------------------------------------')

# PYTHON STRINGS as Sequences of Characters
# Strings share their basic methods of access with other Python ordered sequences of
# objects - lists and tuples. The simplest way of extracting single characters from strings
# (and individual members from any sequence) is to unpack them into corresponding variables.

# Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print('-------------------------------------')

# Accessing Characters in Strings by Index
# - first letter of a string is at 0 index, and the last letter is the length of a string -1
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# If we want to start from right end, we can use negative indexing. -1 is the last index
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

print('-------------------------------------')

# Slicing Python Strings

language = 'Python'
first_three = language[0:3] # start at 0 and goes up to 3, not including the 3
print(first_three)
last_three = language[3:6]
print(last_three)
# another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

print('-------------------------------------')

# Reversing a String

greeting = 'Hello, World!'
print(greeting[::-1])

print('-------------------------------------')

# STRING METHODS
challenge = 'thirty days of python'

# capitalize(): Converts the first character of the string to capital letter
print(challenge.capitalize())

print('-------------------------------------')

# count(): returns occurrences of substrings in string, count(substr, start=.., end=..)
# The start is starting index for couting and end is the last index to count
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

print('-------------------------------------')

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

print('-------------------------------------')

# expandtabs(): Replaces tab characters with spaces, default tab size is 8 -> takes tab size argument
tabs_challenge = 'thirty\tdays\tof\tpython'
print(tabs_challenge.expandtabs())
print(tabs_challenge.expandtabs(10))

print('-------------------------------------')

# find(): returns the index of the first occurrence of a substring, if not returns -1
print(challenge.find('y'))
print(challenge.find('th'))
print(challenge.find('ä'))

print('-------------------------------------')

# rfind(): returns the index of the last occurence of a substring, if not returns -1
print(challenge.rfind('y'))
print(challenge.rfind('th'))

print('-------------------------------------')

# format(): formats string into a nicer output (check examples above)

# index(): returns the lowest index of a substring, additional arguments indicate
#   starting and ending index (default 0 and str len - 1). If the substr is not found
#   it raises a ValueError
sub_string = 'da'
print(challenge.index(sub_string))
try: 
    print(challenge.index(sub_string, 9))
except ValueError:
    print('ValueError')

print('-------------------------------------')

# rindex(): returns the highest index of a substring, additional args indicate starting
#   and ending index (default 0 & strlen -1)
print(challenge.rindex(sub_string))
try: print(challenge.rindex(sub_string, 9))
except ValueError: print('ValueError')
print(challenge.rindex('on', 8))

print('-------------------------------------')

# isalnum(): checks alphanumeric character
alnum_challenge = 'ThirtyDaysPython'
print(alnum_challenge.isalnum())

alnum_challenge = '30DaysPython'
print(alnum_challenge.isalnum())

# challenge = 'thirty days of python'
print(challenge.isalnum()) # false, space is not an alphanumeric character

print('-------------------------------------')

# isalpha(): checks if all string elements are alphabet characters (a-z & A-Z)
print(challenge.isalpha()) # false, space is excluded
print(alnum_challenge.isalpha()) # true
num = '123'
print(num.isalpha()) # numbers are excluded

print('-------------------------------------')

# isdecimal(): checks if all characters in string are decimal (0-9)
unicode = '\u00B2'
print(challenge.isdecimal())
print(num.isdecimal())
print(unicode.isdecimal())
print('12 3'.isdecimal())

print('-------------------------------------')

# isdigit(): checks if all characters in a string are numbers (0-9 and some unicode chars for numbers)
print(challenge.isdigit())
print(num.isdigit())
print(unicode.isdigit())

print('-------------------------------------')

# isnumeric(): checks if all characters in string are numbers or number related
#   (just like isdigit(), just accepts more symbols like ½)
print(num.isnumeric())
print(unicode.isnumeric())
print('10.4'.isnumeric())

print('-------------------------------------')

# isidentifier(): checks for a valid identifier - it checks if a string is a valid variable name
identifier = '30DaysOfPython'
print(identifier.isidentifier()) # False, because it starts with a number
identifier = 'thirty_days_of_python'
print(identifier.isidentifier())

print('-------------------------------------')

# islower(): checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

print('-------------------------------------')

# isupper(): checks if all alphabet characters in the string are uppercase
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

print('-------------------------------------')

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

result = '# '.join(web_tech)
print(result)

print('-------------------------------------')

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythooonnn'
print(challenge.strip('noth')) 

print('-------------------------------------')

# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

print('-------------------------------------')

# split(): splits the string, using given string or space as a separator
print(challenge.split())
print('thirty, days, of, python'.split(', '))

print('-------------------------------------')

# swapcase(): converts all uppercase characters to lowercase and all lowercase chars to uppercase
print(challenge.swapcase())
print('Thirty Days Of Python'.swapcase())

print('-------------------------------------')

# startswith(): checks if string starts with the specified string
print(challenge.startswith('thirty'))
challenge = '30 days of python'
print(challenge.startswith('thirty'))

print('-------------------------------------')
