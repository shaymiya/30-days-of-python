# EXERCISES : DAY 04
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
sample_text = '%s %s %s %s' %('Thirty', 'Days', 'Of', 'Python')
print(sample_text)
print('-------------------------------------')

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
sample_text = '{} {} {}'.format('Coding', 'For', 'All')
print(sample_text)
print('-------------------------------------')

# 3-> Declare a variable company and modify it in code
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

company = company.capitalize()
print(company)
company = company.title()
print(company)
company = company.swapcase()
print(company)
company = company.title()

print(company.strip('Coding '))
if company.find('Coding') == 0:
    print('True')

print('-------------------------------------')

print(company.replace('Coding', 'Python'))
print('Python For Everyone'.replace('Everyone', 'All'))

print(company.split())
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))

print('-------------------------------------')

print(company[0])
print(f'Last index of the company is at index: {len(company) - 1}')
print(company[10])

print('-------------------------------------')

python_slogan = 'Python For Everyone'
coding_slogan = 'Coding For All'

print(f'The first occurrence of C in {coding_slogan} is at index {coding_slogan.find('C')}')
print(f'The first occurrence of F in {coding_slogan} is at index {coding_slogan.find('F')}')
print(f'The last occurrence of l in "Coding For All People" is at index {'Coding For All People'.rfind('l')}')

print('-------------------------------------')

sample_text = 'You cannot end a sentence with because because because is a conjunction'

# Find the position of first occurrence of because in the sample text
print(sample_text.index('because'))
print(sample_text.rindex('because'))

# Slice out the because because because from sample text
print(f'{sample_text[:sample_text.index('because') - 1]} {sample_text[sample_text.rindex('because') + len('because') + 1:]} ')

print('-------------------------------------')

substring = 'Coding'
print(coding_slogan.startswith(substring))
substring = 'coding'
print(coding_slogan.endswith(substring))

print('-------------------------------------')

sample_text = '  Coding For All      '
print(sample_text.strip())

print('-------------------------------------')

print(f'30DaysOfPython is an identifier: {'30DaysOfPython'.isidentifier()}')
print(f'thirty_days_of_python is an identifier: {'thirty_days_of_python'.isidentifier()}')

print('-------------------------------------')

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
sample_text = '# '.join(python_libraries)
print(sample_text)

print('-------------------------------------')

print('I am enjoying this challenge.\nI just wonder what is next.')

print('-------------------------------------')

print('Name\tAge\tCountry\tCity'.expandtabs(10))
print('Shay\t3\tFinland\tToyShelf'.expandtabs(10))

print('-------------------------------------')

radius = 10
pi = 3.14
area = pi * radius ** 2

print('radius = %d' %(radius)) 
print('area = {} * {} ** {}'.format(pi, radius, 2))
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')

print('-------------------------------------')

# using only the most recent string formatting method
a, b = 8, 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

print('-------------------------------------')
