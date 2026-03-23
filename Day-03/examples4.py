# COMPARISON OPERATORS
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)

# In addition to the above comparison operator Python uses:
#   - is: Returns true if both variables are the same object (x is y)
#   - is not: Returns true if both variables are not the same object (x is not y)
#   - in: Returns true if the queried list contains a certain item (x in y)
#   - not in: Returns true if the queried list doesn't have a certain item (x not in y)

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('S in Shay', 'S' in 'Shay')
print('B not in Shay', 'B' not in 'Shay')
print('coding' in 'coding for all')
print('a in an: ', 'a' in 'an')
print('4 is 2 ** 2: ', 4 is 2 ** 2)