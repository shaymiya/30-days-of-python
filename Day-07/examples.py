# DAY 07 : SETS
# Set is a collection of items. Let me take you back to your elementary or high school
# mathematics lesson. The Mathematics definition of a set can be applied also in Python.
# Set is a collection of UNORDERED and UN-INDEXED DISTINCT elements. In Python set is used
# to store unique items, and it is possible to find the UNION, INTERSECTION, DIFFERENCE
# SYMMETRIC DIFFERENCE, SUBSET, SUPER SET and DISJOINT SET among sets.

# CREATING A SET
# To create an empty set, we use the set() function. Empty curly brackets {} will create
# A DICTIONARY !!
st = set()

# Creating a set with initial items:
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

# GETTING SETS LENGTH
# We use len() method to find the length of a set
print(len(fruits))

# ACCESSING ITEMS IN A SET
# We use LOOPS to access items. We will see this in loop section.
for item in fruits:
    print(item)

# CHECKING AN ITEM
# To check if an item exists in a list we use in membership operator.
print('Does set contain mango?', 'mango' in fruits)

# ADDING ITEMS TO A SET
# Once a set is created we can change any items and we can also add additional items
# - Add one item using add()
fruits.add('lime')
print(fruits)

# - Add multiple items using update(). The update() allows to add multiple items to
#       a set. The update() takes a list argument.
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

# REMOVING ITEMS FROM A SET
# We can remove an item from a set using remove() method. If the item is not found 
#   remove() method will rise errors, so it's good to check if the item exists in the
#   given set. However, discard() method doesn't rise any errors!
fruits.remove('tomato')
print(fruits)

# The pop() methods remove a RANDOM item from a list and it returns the removed item.
fruits.pop() # removes a random item from the set
print(fruits)

print(fruits.pop())
print(fruits)

# If we are interested in the removed item
removed_item = fruits.pop()
print(removed_item)
print(fruits)

# CLEARING ITEMS IN A SET
# If we want to clear a or empty a set we use clear() method
fruits.clear()
print(fruits)

# DELETING A SET
# If we want to delete the set itself, we use del operator
del fruits
try: print(fruits)
except NameError: print('NameError: The set "fruits" has been deleted')

# CONVERTING LIST TO SET
# We can convert list to set and set to list. Converting list to set REMOVES DUPLICATES
# and only unique items will be reserved.
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(fruits)
fruits = set(fruits)
print(fruits)

# JOINING SETS
# We can join two sets using the union() or update() method or | symbol

# - union(): This method returns a new set
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits_and_vegetables = fruits | vegetables
print(fruits_and_vegetables) # OR
print(fruits.union(vegetables)) # OR
print(fruits | vegetables)

# - update(): This method inserts a set into a given set
fruits.update(vegetables)
print(fruits)

# FINDING INTERSECTION ITEMS
# Intersection returns a set of items which are in BOTH the sets. You can also use
#   & symbol
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers= {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # OR
print(whole_numbers & even_numbers)

print(set('python').intersection(set('dragon')))

# CHECKING SUBSET AND SUPER SET
# A set can be a subset or super set of other sets
# - Subset: issubset()
# - Super set: issuperset()
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

# CHECKING THE DIFFERENCE BETWEEN TWO SETS
# Returns the difference between two sets. You can also use the - symbol
print(whole_numbers.difference(even_numbers)) # OR
print(whole_numbers - even_numbers)

# FINDING SYMMETRIC DIFFERENCE BETWEEN TWO SETS
# Returns the symmetric difference between two sets. This means that it returns a set
# that contains all items from both sets, EXCEPT items that are present in both sets
# Mathematically: (A\B) U (B\A)
# (this kinda combines the previous differences?)
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

python = set('python')
dragon = set('dragon')
print(python.symmetric_difference(dragon))

# JOINING SETS
# If two sets do not have a common item or items, we call them DISJOINT SETS. We can
# check if two sets are joint or disjoint using isdisjoint() method
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))

print(python.isdisjoint(dragon))
