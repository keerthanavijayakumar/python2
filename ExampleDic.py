my_dict = {'name': 'KEERTHANA', 'age': 22}

# Output: KEERTHANA
print(my_dict['name'])

# Output: 22
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))


