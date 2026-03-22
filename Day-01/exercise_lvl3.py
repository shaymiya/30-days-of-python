# EXERCISE : LEVEL 3

int_sample = 1
float_sample = 2.3
complex_sample = 1 + 1j

string_sample = "This is me working on some coding letsgooo"
boolean_sample = True
list_sample = [int_sample, float_sample, complex_sample, string_sample, boolean_sample]

for item in list_sample:
    print(f'Type: {type(item)} - Sample: {item}')

tuple_sample = ('These', 'are', 'locked', 'values')

for item in tuple_sample:
    print(item)

set_sample = {'These', 'are', 'only', 'unique', 'and', 'unordered', 'items'}

for item in set_sample:
    print(item)

dictionary_sample = {1: 'one', 2: 'two', 3: 'three'}

for item in dictionary_sample:
    print(dictionary_sample[item])

# Finding Euclidean distance between (2, 3) and (10, 8)
c = ((2 - 10)**2 + (3 - 8)**2)**(1/2)

print(c)