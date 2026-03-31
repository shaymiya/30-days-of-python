# EXERCISES : DAY 13

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_list = [i for i in numbers if i <= 0]
print(filtered_list)

print('--------------------------------')

# Flatten the following list of lists to a one dimensional list
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [n for r in list_of_lists for n in r]
print(flattened_list)

print('--------------------------------')

list_of_tuples = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(list_of_tuples)

print('--------------------------------')

# Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [list(c) for l in countries for c in l]
flattened_list = [[c[0].upper(), c[0][:3].upper(), c[1].upper()] for c in flattened_list]
print(flattened_list)

print('--------------------------------')

# Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dicts = [list(c) for r in countries for c in r]
list_of_dicts = [{'country': c[0].upper(), 'city': c[1].upper()} for c in list_of_dicts]
print(list_of_dicts)

print('--------------------------------')

# Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_strings = [list(l) for r in names for l in r]
concatenated_strings = [(f'{n[0]} {n[1]}') for n in concatenated_strings]
print(concatenated_strings)

print('--------------------------------')

# Write a lambda function which can solve a slope or y-intercept of linear functions
slope = lambda y, x, b: x / y if y != 0 else x
print('Slope of function 2y = 4x + 6:', slope(2, 4, 6))
print('Slope of function y = 4x + 6:', slope(0, 4, 6))

print('--------------------------------')

y_intercept = lambda y, x, b: b if y == 0 else b / y
print('Y-intercept of function 2y = 4x + 6:', y_intercept(2, 4, 6))
print('Y-intercept of function y = 4x - 6:', y_intercept(0, 4, -6))

print('--------------------------------')
