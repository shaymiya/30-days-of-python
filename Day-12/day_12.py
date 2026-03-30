# EXERCISES : DAY 12

print('--------------------------------')

# Exercises : Level 1
# Write a function which generates a six digit/character random_user_id
from random import randint
from string import digits, ascii_letters as letters

def random_user_id():
    char_collection = digits + letters
    # print(char_collection)
    id = ''
    # 6 digits/numbers
    for i in range(6):
        id += char_collection[randint(0, len(char_collection) - 1)]

    return id

print(random_user_id())

print('--------------------------------')

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn't
# take any parameters but it takes two inputs using input(). One of the inputs is the
# number of characters and the second input is the number of IDs which are supposed to
# be generated
def user_id_gen_by_user():
    char_collection = digits + letters
    ids = []
    id = ''
    result = '==================='

    # Get the number of characters in ids
    chars = int(input('How many characters per id? > '))
    amount = int(input('How many ids do you want to generate? > '))

    # Generate IDs
    for i in range(amount):
        for c in range(chars):
            id += char_collection[randint(0, len(char_collection) - 1)]
        ids.append(id)
        result += f'\n{id}'
        id = ''
        # print('ID generated')
    
    return result

print(user_id_gen_by_user())

print('--------------------------------')

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging
# from 0 to 255 each)
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f'({r},{g},{b})'

print(rgb_color_gen())

print('--------------------------------')

# EXERCISES : LEVEL 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors
# in an array (six hexadecimal numbers written after #). Hexadecimal numeral system is
# made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
def list_of_hexa_colors(num = 1):
    hexadecimals = '0123456789abcdef'
    hexa_list = []
    color = '#'
    for i in range(num):
        for c in range(6):
            color += hexadecimals[randint(0,len(hexadecimals) - 1)]
        # insert the color in the list
        hexa_list.append(color)
        color = '#'
    return hexa_list

print(list_of_hexa_colors(3))

# Do the same for rgb colors
def list_of_rgb_colors(num = 1):
    rgb_list = []
    color = 'rgb('
    for i in range(num):
        r, g, b = str(randint(0,255)), str(randint(0,255)), str(randint(0,255))
        color += f'{r}, {g}, {b})'
        rgb_list.append(color)
        color = 'rgb('
    return rgb_list

print(list_of_rgb_colors(3))

print('--------------------------------')

# Write a function generate_colors which can generate any number of hexa or rgb colors
def generate_colors(type, num):
    if type.lower() == 'hexa':
        print(list_of_hexa_colors(num))
    elif type.lower() == 'rgb':
        print(list_of_rgb_colors(num))
    else:
        print(f'{type} and {num} are not supported in this function')

generate_colors('hexa', 4)
generate_colors('rgb', 4)
generate_colors('test', 'test')

print('--------------------------------')

# EXERCISES : LEVEL 3
# Call your function shuffle_list. It takes a list as a parameter and returns a suffled
# list
def shuffle_list(list):
    suffled_list = []
    for item in list:
        suffled_list.insert(randint(0, len(list)-1), item)
    return suffled_list

test_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(shuffle_list(test_list))

print('--------------------------------')

# Write a function which returns an array of seven random numbers in a range of 0-9.
# All the numbers must be unique
def generate_numbers():
    nums = []
    print('Generating numbers...')
    i = 1 # for debugging
    while len(nums) < 7:
        # print(f'Round {i}')
        random_number = randint(0,9)
        if random_number not in nums:
            nums.append(random_number)
        i += 1 # for debugging

    return nums

print(generate_numbers())            

print('--------------------------------')
