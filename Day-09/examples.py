# DAY 09 - CONDITIONALS
# By default, statements in Python script are executed sequentially from TOP TO BOTTOM.
# If the processing logic require so, the sequential flow of execution can be altered in
# TWO ways:
# 
# - Conditional execution: a block of one or more statements will be executed
#       IF A CERTAIN EXPRESSION is TRUE (e.g. num % 2 == 0, value > 0)
# 
# - Repetitive execution: a block of one or more statements will be repetitively
#       executed as long as a certain expression is true. (e.g. playing == True)
# 
# In this section, we will cover if, else, elif statements. The COMPARISON and LOGICAL
# operators we learned in previous sections will be useful here!

# IF CONDITION
# In python and other programming languages the key word 'if' is used to check if a condition
# is true and to decide whether or not to execute the block of code following the statement.
# NOTE! Remember the INDENTATION after the colon!

a = 3
if a > 0:
    print('A is a positive number')

# Since 3 is greater than 0, the code block was executed. However, if the condition is false
# we don't se the result. In order to see the result of a falsy condition, we will use
# another block of code, which will be placed under the ELSE statement

# IF ELSE
# If condition is true, the first block will be executed, if not the else condition will run
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# Since 3 is not lesser than 0, the else -code block will run. But what if we want to have
# more than 2 conditions? 

# IF ELIF ELSE
# In our daily life, we make decisions by checking multiple conditions. And similarly to our
# daily life, programming is also full of conditions. This calls for another conditional statement:
# elif
a = 0

if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# SHORT HAND
# We can use a short hand for simple conditional checks
a = 3
print('A is positive') if a > 0 else print('A is negative')

# NESTED CONDITIONS
# Conditions can be nested
a = 0

if a > 0:
    if a % 2 == 0:
        print('A is positive and even number')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# We can avoid writing nested conditions by using logical operator and

# IF CONDITION AND LOGICAL OPERATORS
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative integer')

# IF AND OR LOGICAL OPERATORS
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied.')
