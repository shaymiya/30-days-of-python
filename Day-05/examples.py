# DAY 05 - LISTS
# There are 4 collection data types in python
# - List: a collection which is ordered and changeable. Allows duplicate members
# - Tuple: ordered collection which is unchangeable and unmodifiable. Allows duplicate members
# - Set: UNORDERED collection which is un-indexed and unmodifiable, but we can add new items to the set.
#        Duplicate memberes are NOT allowed.
# - Dictionary: UNORDERED collection which is changeable AND indexed. NO duplicate members

# A list is collection of DIFFERENT data types which is ORDERED and MODIFIABLE(mutable).
# A list can be empty or it may have different data type items.

# HOW TO CREATE LIST
# 1. using list built in function
lst = list()
empty_list = list() # empty list, no item in the list
print(len(empty_list))

# 2. using square brackets []
lst = []
empty_list = []
print(len(empty_list))

print('-------------------------------------')

# Lists with initial values. len() can be used to find the length of a list
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'meat', 'butter']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# print the lists and its length (nbr of entries)
print('Fruits: ', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetables: ', vegetables)
print('Number of vegetables: ', len(vegetables))
print('Animal Products: ', animal_products)
print('Number of animal products: ', len(animal_products))
print('Web technologies: ', web_techs)
print('Number of web technologies: ', len(web_techs))
print('Countries: ', countries)
print('Number of countries: ', len(countries))

print('-------------------------------------')

# Lists can have items of different data types
lst = ['Shay', 3, True, {'country': 'Finland', 'city': 'ToyShelf'}]
print(lst)

print('-------------------------------------')

# ACCESSING LIST ITEMS

# Positive indexing
first_fruit = fruits[0]
print(first_fruit)

# Negative indexing
last_fruit = fruits[-1]
print(last_fruit)

print('-------------------------------------')

# UNPACKING LIST ITEMS
# First example
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

print('-------------------------------------')

# second example
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

print('-------------------------------------')

#third example
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

print('-------------------------------------')

# SLICING ITEMS FROM A LIST
# - Positive indexing: we can specify a range of positive indexes by specifying the start,
#       end and step, the return value will be a NEW LIST.
#       (default values for start = 0, end = len(lst) -1, step = 1)
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
# this will give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop, it takes all the rest
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[1::2] # third argument specifies step. This will take every 2nd item

# - Negative indexing: We can specify a range of negative indexes by specifying the start, end and step
#       the return value will be a NEW LIST
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1] # NEGATIVE STEP will take the list in reverse order!

# MODIFYING LISTS
# List is a mutable ordered collection of items.
print(fruits)
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'line'
print(fruits)

print('-------------------------------------')

# CHECKING ITEMS IN A LIST
# Checking if an item is part of a list is done using 'in' operator
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

print('-------------------------------------')

# ADDING ITEMS TO A LIST
# We can add items to the end of the list using append()-method!
print(fruits)
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

print('-------------------------------------')

# INSERTING ITEMS INTO A LIST
# We can use insert()-method to insert a SINGLE item at a specified index in a list.
# Note that other items are sifted to the RIGHT. The insert() method takes two argumets:
#   index and an item to insert
print(fruits)
fruits.insert(2, 'avocado')
print(fruits)
fruits.insert(3, 'watermelon')
print(fruits)

print('-------------------------------------')

# REMOVING ITEMS FROM A LIST
# The remove() method removes a specified item from a list
print(fruits)
fruits.remove('banana') # this method removes THE FIRST OCCURRENCE of the item on a list
print(fruits)
fruits.remove('watermelon')
print(fruits)

print('-------------------------------------')

# REMOVING ITEMS USING POP
# The pop() method removes the specified index, or the LAST ITEM if the index is NOT specified
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

print('-------------------------------------')

# REMOVING ITEMS USING DEL
# The del keyword removes the specified index and it can also be used to delete items
# within index range. It can also delete the list COMPLETELY!
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3] # this deletes items BETWEEN given indexes, so it doesn't delete index 3!
print(fruits)
del fruits
try: print(fruits) # This should give: NameError: name 'fruits' is not defined
except NameError: print('NameError: The list has been deleted!')

print('-------------------------------------')

# CLEARING LIST ITEMS
# The clear() method empties the list
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
fruits.clear()
print(fruits)

print('-------------------------------------')

# COPYING A LIST
# It is possible to copy a list by reassigning it to a new variable in the following way:
#   list2 = list1. Now list2 is a REFERENCE of list1, any changes we make in list2 will also
#   modify the original, list1. But there are lots of cases in which we do not like to modify
#   the original - instead we like to have a different copy. One way of avoiding the problem
#   is using copy() method.
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
fruits_copy = fruits.copy()
print(fruits_copy)

print('-------------------------------------')

# JOINING LISTS
# There are several ways to join, or concatenate, two or more lists in python
# - Plus Operator (+)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# - Joining using extend() method. The extend method allows to append list in a list.
num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

print('-------------------------------------')

# COUNTING ITEMS IN A LIST
# The count() method returns the number of times an item appears in a list:
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

print('-------------------------------------')

# FINDING INDEX OF AN ITEM
# The index() method returns the index of an item in the list
print(fruits.index('orange'))
print(ages.index(24))

print('-------------------------------------')

# REVERSING A LIST
# The reverse() method reverses the order of a list
print(fruits)
fruits.reverse()
print(fruits)

print('-------------------------------------')

# SORTING LIST ITEMS
# To sort lists we can use sort() method or sorted() built-in functions. The sort() method
#   reorders the list items in ascending order and modifies the ORIGINAL LIST. If an argument
#   of sort() method reverse is equal to true, it will arrange the list in descending order

# - sort(): this method modifies the original list
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

print(ages)
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

print('-------------------------------------')

# - sorted(): returns the ordered list WITHOUT MODIFYING THE ORIGINAL LIST
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
# Reverse order:
print(sorted(fruits, reverse=True))

print('-------------------------------------')
