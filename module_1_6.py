my_dict = {'Andrey' : 2012, 'Max' : 1988, 'Julia' : 1987, 'Anjelika' : 2024}
print('Dict:', my_dict)
print('Existing value:', my_dict['Max'])
print('Not existing value:', my_dict.get('Anna'))
print('Deleted value:', my_dict.pop('Max'))

my_dict.update({'Natalia' : 1978,
                'Vladimir' : 1977})
print('Modified dictionary:', my_dict)
print()

my_set = {1, 3, 3, 'Apple', float(1.23), 'Apple', float(1.23)}
print('Set:', my_set)
my_set.update([5, (3, 2, 1)])
my_set.discard(1)
print('Modified set:', my_set)

