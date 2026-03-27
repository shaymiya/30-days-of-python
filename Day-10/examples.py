# DAY 10 : LOOPS
# In order to handle repetitive tasks, programming languages use LOOPS. Python also
# provides the following types of TWO loops:

# 1. while loop
# 2. for loop

# WHILE LOOP
# We use the reserved word while to make a while loop. It is used to execute a block
# of statements repeatedly until a given condition is satisfied. When the condition
# becomes false, the lines of code after the loop will be continued to be executed.

count = 0
while count <= 5:
    print(count)
    count += 1

print('----------------------------')

# In the above while loop the condition becomes false when count is over 5. That is when
# the loop stops. If we are interested to run block of code once the condition is no longer
# true, we can use ELSE (?? huh)

count = 0
while count <= 5:
    print(count)
    count += 1
else:
    print(count)

print('----------------------------')

# The above loop condition will be false when count is 6 and the loop stops, and execution
# starts the else statement. As a result 6 will be printed.

# BREAK AND CONTINUE - PART 1
# - Break: We use break when we like to get out of or stop the loop
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

# The above while loop only prints 0, 1, 2, but when it reaches 3 it stops

print('----------------------------')

# - Continue: With the continue statement we can skip the current iteration and
#   continue with the next:
count = 0
while count <= 10:
    if count % 2 != 0:
        count += 1
        continue
    print(count)
    count += 1

print('----------------------------')

# FOR LOOP
# A for keyword is used to make a for loop, similar with other programming languages,
# but with some syntax differences. Loop is used for iterating over a sequence (that
# is either a list, a tuple, a dictionary, a set or a string)

# Using For loop on list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number is a temporary name to refer to the list's items
    print(number)

print('----------------------------')

# Using for loop on a string
language = 'Python'
for letter in language:
    print(letter)

print('--')

# OR
for i in range(len(language)):
    print(language[i])

print('----------------------------')

# Using for loop on tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

print('----------------------------')

# Using for loop with dictionary. Looping through a dictionary gives you the
#   key of the dictionary
person = {
    'first_name': 'Shay',
    'last_name': 'Miya',
    'age': 3,
    'country': 'Finland',
    'skills': ['HTML','CSS', 'Eating sweets'],
    'address':{
        'city': 'ToyShelf',
        'street': 'Plushie Road'
    }
}

for key in person:
    print(key)

print('----------------------------')

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

print('----------------------------')

# Using for loop in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print(company)

print('----------------------------')

# BREAK AND CONTINUE - PART 2
# Break: used when we want to break out of our loop before it is completed
print(numbers)
for number in numbers:
    print(number)
    if number == 3:
        break

print('----------------------------')

# Continue: used when we want to skip some of the steps in the iteration of the loop
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")

print('outside the loop')

# in the example above, if the number == 3, the step AFTER the condition (but inside
# the loop) is skipped and the execution of the loop continues if there are any iterations left

print('----------------------------')

# THE RANGE FUNCTION
# The range() function is used to return a list of numbers. The range(start, end, step)
# takes 3 parameters: starting, ending and increment. By default it starts from 0 and
# the increment is 1. The range sequence needs at least 1 argument (end).

# Creating sequences using range:
lst = list(range(11))
print(lst)

st = set(range(1,11)) # 2 arguments = start & end
print(st)

lst = list(range(0,11,2))
print(lst)
st = set(range(0,11,2))
print(st)

# for backward from start to end
lst = list(range(11,0,-2))
print(lst)

# in for loops
for number in range(11):
    print(number)

print('----------------------------')

# NESTED FOR LOOPS
# We can write loops inside a loop

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

print('----------------------------')

# FOR ELSE (??? again??)
# If we want to execute some message when the loop ends, we use else
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)

print('----------------------------')

# PASS
# In python when statement is required (after semicolon), but we don't like to
# execute any code there, we can write the word PASS to avoid errors.
# Also we can use it as a PLACEHOLDER, for future statements:
for number in range(6):
    pass
else:
    print('Testing pass keyword')

print('----------------------------')
