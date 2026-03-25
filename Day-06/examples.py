# DAY 6 : TUPLES
# A tuple is a collection of different data types which is ordered and unchangeable
# (immutable). Tuples are written with round brackets, (). Once a tuple is created,
# we cannot change its values. We cannot use add, insert, remove methods in tuple
# because it is not modifiable (mutable). Unlike list, tuple has few methods.

# Methods related to tuples:
# - tuple(): to create an empty tuple
# - count(): to count the number of a specified item in a tuple
# - index(): to find the index of a specified item in a tuple
# - + operator: to join two or more tuples and to create a new tuple

# CREATING A TUPLE
# - Empty tuple:
empty_tuple = () # or
empty_tuple = tuple()

# - Tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)

# TUPLE LENGTH
# We use the len() method to get the length of a tuple
print(len(fruits))

# ACCESSING TUPLE ITEMS
# - positive & negative indexing (similar to lists)
first_fruit = fruits[0]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)

# SLICING TUPLES
# We can slice out a sub-tuple by specifying a range of indexes where to start andi
# where to end in the tuple, the return value will be a new tuple with the specified
# items.

# Range of Positive & Negative Indexes
print(fruits)
all_fruits = fruits[0:] # or fruits[-4:]
orange_mango = fruits[1:3]
print(orange_mango)
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)

print(fruits[::-1]) # prints the tuple in reverse!

# CHANGING TUPLES TO LISTS
# We can change tuples to lists and lists to tuples. Tuple is immutable, so if we
# want to modify a tuple we should change it to a list.
fruits = list(fruits)
print(fruits)
fruits.append('apple')
print(fruits)
fruits = tuple(fruits)
print(fruits)

# CHECKING AN ITEM IN A TUPLE
# We can check if an item exists or not in a tuple using in, it returns a boolean
print('orange' in fruits)
print('avocado' in fruits)
try: fruits[0] = 'avocado'
except TypeError: print('TypeError: Tuple does not support item assignment!')

# JOINING TUPLES
# We can join two or more tuples using + operator
print(fruits)
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
print(vegetables)
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# DELETING TUPLES
# It is not possible to remove a single item in a tuple but it is possible to delete
# the tuple itself using del
print(vegetables)
del vegetables
try: print(vegetables)
except NameError: print('NameError: Tuple does not exist anymore')
