# Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с различным количеством аргументов
print_params()  # Вызываем без аргументов
print_params(14)  # Передаем только первый аргумент
print_params(b=25)  # Передаем только второй аргумент
print_params(c=[1, 2, 3])  # Передаем только третий аргумент
print_params(12, 'string')  # Передаем первые два аргумента

# Распаковка параметров
values_list = [3.14, 'strong', True]
values_dict = {'a': 44, 'b': 'word', 'c': False}

# Передаем список и словарь в функцию с распаковкой
print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря

# Распаковка и отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Распаковка списка и передача третьего аргумента

def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []  # Создаем новый список, если list_my = None
    list_my.append(item)  # Добавляем элемент
    return list_my  # Возвращаем измененный список


# Примеры использования функции
list_1 = append_to_list(1)
list_2 = append_to_list(2)
# Передаем новый список
list_3 = append_to_list(3, values_list_2) 
list_4 = append_to_list(6, values_list_2)
list_5 = append_to_list(67, values_list_2)

print("Список 1: ", list_1)
print("Список 2: ", list_2)
print("Список 3: ", list_3)
