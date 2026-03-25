# EXERCISES : DAY 5

empty_list = []
not_so_empty_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Length of the not so empty list: ', len(not_so_empty_list))

print('-------------------------------------')

first_item = not_so_empty_list[0]
print('First item: ', first_item)
middle_item = not_so_empty_list[int(len(not_so_empty_list)/2)]
print('Middle item: ', middle_item)
last_item = not_so_empty_list[-1]
print('Last item: ', last_item)

print('-------------------------------------')

mixed_data_types = ['Shay', 3, 100, False, {'country': 'Finland', 'city': 'ToyShelf'}]
print(mixed_data_types)

print('-------------------------------------')

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print('Number of companies in the list: ', len(it_companies))
print('First company: ', it_companies[0])
print('Middle company: ', it_companies[int(len(it_companies)/2)])
print('Last company: ', it_companies[-1])

# modify one of the companies
print(it_companies)
it_companies[it_companies.index('Oracle')] = 'Opera'
print(it_companies)

# add an it-company to companies
it_companies.append('Oracle')
print(it_companies)

# add a company in the middle of the list
it_companies.insert(int(len(it_companies)/2), 'Nokia')
print(it_companies)

# change one of the companies into uppercase
it_companies[it_companies.index('Nokia')] = it_companies[it_companies.index('Nokia')].upper()
print(it_companies)

# join the it-companies with '#; '
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# check if a certain company exists in the list
if it_companies.count('Facebook') > 0:
    print('The company "Facebook" exists in the list')
else:
    print('The company does not exist in the list')

# sort the list with sort() method
it_companies.sort()
print(it_companies)

# reverse the list
it_companies.reverse()
print(it_companies)

# slice out the first 3 companies in the list
sliced_companies = it_companies.copy()
del sliced_companies[:3]
print(sliced_companies)

# slice out the last 3 companies in the list
del sliced_companies[-3:]
print(sliced_companies)

# slice out the middle company from the list
del sliced_companies[int(len(sliced_companies)/2)]
print(sliced_companies)

print('-------------------------------------')

# remove the first company from the list
print(it_companies)
popped_companies = it_companies.copy()

popped_companies.pop(0)
print(popped_companies)

# remove the middle company from the list
popped_companies.pop(int(len(popped_companies)/2))
print(popped_companies)

# remove the last company from the list
popped_companies.pop(-1)
print(popped_companies)

# remove all the companies from the list
popped_companies.clear()
print(popped_companies)

# destroy the companies list
del popped_companies
try: print(popped_companies)
except NameError: print('Popped companies successfully destroyed')

print('-------------------------------------')

# join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
all_ends = front_end + back_end
print(all_ends)

# copy the joined list and insert Python and SQL after Redux
full_stack = all_ends.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')
print(full_stack)

print('-------------------------------------')

# EXERCISES: LEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

# sort the list and find the min and max age
ages.sort()
print(ages)
print('Min age: ', ages[0])
print('Max age: ', ages[-1])

# add the min and max age again to the list
ages.insert(0, ages[0])
ages.insert(-1, ages[-1])
print(ages)

# find the median age
def find_middle(list):
    return int(len(list)/2)

if len(ages) % 2 == 0:
    median_age = ( ages[find_middle(ages)] + ages[find_middle(ages) + 1] ) / 2
else:
    median_age = ages[find_middle(ages)]

print('Median age: ', median_age)

# find the average age (sum of all ages divided by their number)
average_age = sum(ages) / len(ages)
print('Average age: ', average_age)

# find the range of ages (max minus min)
age_range = ages[-1] - ages[0]
print('Range of the ages: ', age_range)

# compare the value of (min - average) and (max - average), use abs() method
print('Range of the ages from min: ', abs(ages[0] - average_age))
print('Range of the ages from max: ', abs(ages[-1] - average_age))

print('-------------------------------------')

# find the middle country(ies) in the countries list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
if len(countries) % 2 != 0:
    print(countries[find_middle(countries)])
else:
    print(countries[find_middle(countries)] + ', ' + countries[find_middle(countries) + 1])

first_half = countries[:find_middle(countries) + 1]
second_half = countries[find_middle(countries) + 1:]
print(first_half)
print(second_half)

print('-------------------------------------')

# unpack the first 3 countries and print the rest as scandic countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries
print(ch)
print(ru)
print(us)
print(*scandic)

print('-------------------------------------')
