# EXERCISES : DAY 7
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises : Level 1

# Find the length of the set it_companies
print(f'The number of it-companies in the set is {len(it_companies)}')
print(it_companies)

# Add Twitter to it companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set
it_companies.update(['Opera', 'Mozilla', 'Safari'])
print(it_companies)

print('------------------------------------')

# Remove one of the companies from the set
it_companies.remove('Safari')
print(it_companies)

try: it_companies.remove('Safari')
except KeyError: print('KeyError: Can not find Safari from the set')

it_companies.discard('Safari') # Doesn't rise errors! Maybe better to use this?
print(it_companies)

print('------------------------------------')

# Exercises : Level 2

# Join A and B
C = A | B
print(C) # OR
print(A | B) # OR
print(A.union(B))

print('------------------------------------')

# Find A intersection B
print(A.intersection(B)) # OR
print(A & B)

print('------------------------------------')

# Is A subset of B
print('Is A subset of B? ', A.issubset(B))

print('------------------------------------')

# Are A and B disjoint sets
print('Are A and B disjoint sets? ', A.isdisjoint(B))

print('------------------------------------')

# Join A with B and B with A
print(A | B)
print(B | A)

print('------------------------------------')

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

print('------------------------------------')

# Delete the sets completely
A.clear()
print(A)

del A
del B

try: print(B)
except NameError: print('NameError: Set B does not exist')

print('------------------------------------')

# Exercises : Level 3

# Convert the ages to a set and compare the length of the list and the set,
# which one is bigger?
ages_set = set(age)
print(len(age))
print(len(ages_set))

# ANSWER: converting a list to a set removes duplicate values. This means that the
#         original list is bigger.

print('------------------------------------')

# Explain the difference between the following data types: string, list, tuple, set
# ANSWER: string is an ordered and mutable collection of characters (char), a list is an ordered
#         and mutable collection of different types of data (strings, integers, lists, etc),
#         tuple is an ordered UNMUTABLE collection of different types of data and a 
#         set is an UNORDERED and MUTABLE collection of UNIQUE items that can also hold
#         different types of data!
test_set = {True, 'Testing', ('red', 1, False), 200}
print(test_set)

print('------------------------------------')

# How many unique words have been used in the sentence? Use the split methods and
#   set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
unpacked_sentence = sentence.split(' ')
print(unpacked_sentence)

# let's get the number of unique words by converting the list into a set
unpacked_sentence = set(unpacked_sentence)
print(f'The sentence "{sentence}" has {len(unpacked_sentence)} unique words, the words being {unpacked_sentence}')

print('------------------------------------')
