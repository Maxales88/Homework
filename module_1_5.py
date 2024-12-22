immuable_var = (1, 'string', True)
print(immuable_var)

# immutable_var.append(False) - Операция невозможна, неизменяемый тип данных
# immutable_var[1] = 'strong' - Операция невозможна, неизменяемый тип данных

mutable_list = [1, 2, 'list', False]
print(mutable_list[0])
mutable_list.extend(['banana'])
print(mutable_list)
mutable_list[1] = 'apple'
print(mutable_list)