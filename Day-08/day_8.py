# EXERCISES : DAY 08

# Create an empty dictionary called dog
dog = {}

# Add following things to the dog dictionary:
dog['name'] = 'Spot'
dog['breed'] = 'Kiinankarvakorva'
dog['legs'] = 4
dog['age'] = 1

print(dog)

print('--------------------------------------')

# Create a student dictionary with the following keys:
student = {
    'first_name': 'Eric', 
    'last_name': 'Example', 
    'gender': 'male',
    'age': 19,
    'marital_status': False,
    'skills': ['HTML', 'Python', 'Makes mean waffles'],
    'country': 'USA',
    'city': 'Chicago',
    'address': {
        'street': 'Sample Avenue',
        'house_number': '5 C'
    }
}

# check the length
print('Keys in a student dictionary: ', len(student))

# get value of skills and check the data type (should be a list)
print(f'Skills: {student.get('skills')} \nSkills data type: {type(student['skills'])}')

# add 1-2 skills to the student
student['skills'].append('Washing dishes')
student['skills'].append('Horse Handling')
print('Skills:', student['skills'])

print('--------------------------------------')

# get the dictionary keys & values as a list
print(student.keys())
print(student.values())

# change the dictionary to a list of tuples
student_list = student.items()
print(student_list)

print('--------------------------------------')

# delete one of the items in a dictionary
del student['marital_status']
del student

try: print(student)
except NameError: print('NameError: A dictionary "student" does not exist')
 