# DAY 8 : DICTIONARIES
# A dictionary is a collection of UNORDERED, MODIFIABLE (mutable) PAIRED (key:value)
# data types.

# CREATING A DICTIONARY
# To create a dictionary we use curly brackets {}, or the dict() built-in function
empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2'}

person = {
    'first_name': 'Shay',
    'last_name': 'Miya',
    'age': 3,
    'is_married': False,
    'skills': ['HTML', 'CSS', 'C++ (moderate)', 'Python (learning)'],
    'address': {
        'country': 'Finland',
        'city': 'ToyShelf'
    }
}

# Dictionary can include ANY DATA TYPES, including a dictionary!

# DICTIONARY LENGTH
# Checks the number of key:value pairs in the dictionary
print(len(person))

print('-------------------------------')

# ACCESSING DICTIONARY ITEMS
# We can access Dictionary items by referencing to its key name
print(person['first_name'])
print(person['age'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['country'])
try: print(person['city'])
except KeyError: print('KeyError: The selected entry does not exist in person directory')

print('-------------------------------')

# Accessing an item by key name raises an error if the key does not exist.
# To avoid this error first we have to check if a key exist or we can use the
# get() method. The get method returns None, which is a NoneType object data type
# if the key does not exist.
# OH I SEE, so this is the better method in accessing stuff?

print(person.get('first_name'))
print(person.get('skills'))
print(person.get('city'))

print('-------------------------------')

# ADDING ITEMS TO A DICTIONARY
# We can add new key and value pairs to a dictionary
person['job_title'] = 'Student'
person['skills'].append('C#')
print(person)

print('-------------------------------')

# MODIFYING ITEMS IN A DICTIONARY
# We can modify items in a dictionary
person['age'] = 3.5
person['first_name'] = 'SHAY'
print(person.get('first_name'))
print(person.get('age'))

print('-------------------------------')

# REMOVING KEY AND VALUE PAIRS FROM A DICTIONARY
# - pop(key): removes the item with the specified key name
# - popitem(): removes the last item
# - del: removes an item with specified key name
print(person)
person.pop('first_name')
print(person)
person.popitem()
print(person)
del person['is_married']
print(person)

print('-------------------------------')

# CHANGING DICTIONARY TO A LIST OF ITEMS
# The items() method changes dictionary to a list of tuples
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())

print('-------------------------------')

# CLEARING A DICTIONARY
# If we don't want the items in a dictionary we can clear them using clear() method
dct_2 = dct.copy()
print(dct_2)
print(dct_2.clear())

print('-------------------------------')

# DELETING DICTIONARY
# If we do not use the dictionary we can delete it completely
del dct_2
try: print(dct_2)
except NameError: print('NameError: Dictionary has been deleted')

print('-------------------------------')

# COPY A DICTIONARY
# We can copy a dictionary using a copy() method. By using copy we can avoid mutation
# of the original dictionary
dct_copy = dct.copy()
print(dct_copy)

print('-------------------------------')

# GETTING DICTIONARY KEYS AS A LIST
# The keys() method gives us all the keys of a dictionary as a list
keys = dct.keys()
print(keys)

print('-------------------------------')

# GETTING DICTIONARY VALUES AS A LIST
# The values() method gives us all the values of a dictionary as a list
values = dct.values()
print(values)

print('-------------------------------')
