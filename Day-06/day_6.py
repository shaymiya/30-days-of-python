# EXERCISES: DAY 6

# Exercises: Level 1
empty_tuple = ()

sisters = ('PandaSis', 'Nax', 'Ai')
brothers = ('Theus', 'Joakim', 'Fray')

siblings = sisters + brothers

print(f'I have {len(siblings)} siblings!')

siblings = list(siblings)
family_members = siblings.copy()
family_members.insert(0, 'Cofi')
family_members.insert(1, 'PandaMa')
family_members.insert(2, 'PandaPa')

siblings = tuple(siblings)
family_members = tuple(family_members)
print(siblings)
print(family_members)

print('-----------------------------------')

# Exercises: Level 2

# Unpack siblings and parents from family members
mama, mom, dad, *rest = family_members
print(family_members)
print(mama)
print(rest)

print('-----------------------------------')

# Create fruits, vegetables and animal products tuples. Join the three tuples and
#   assign it to a variable called food_stuff_tp
fruits = ('apple', 'banana', 'kiwi', 'lime')
vegetables = ('cucumber', 'tomato', 'potato')
animal_products = ('milk', 'meat', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print('-----------------------------------')

# Slice out the middle item(s) from the food_stuff tuple or list
print('Items in food stuff: ', len(food_stuff_lt))

if len(food_stuff_lt) % 2 == 0: # if even, there are 2 items in a middle
    del food_stuff_lt[int(len(food_stuff_lt) / 2)]
    del food_stuff_lt[int(len(food_stuff_lt) / 2) + 1]
else:
    # if odd, there is only one thing in the middle
    del food_stuff_lt[int(len(food_stuff_lt) / 2)]
    
print(food_stuff_lt)

# Slice out the first 3 items and the last 3 items from food_stuff_lt list
del food_stuff_lt[0:3]
del food_stuff_lt[-3:]

print(food_stuff_lt)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

print('-----------------------------------')

# Check if Estonia is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Is Estonia a nordic country? ', 'Estonia' in nordic_countries)
print('Is Iceland a nordic country? ', 'Iceland' in nordic_countries)
