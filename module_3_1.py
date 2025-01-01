# Глобальная переменная для подсчета вызовов функций
calls = 0

def count_calls(): # Подсчитывающая функция
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Подсчитываем вызов функции
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return [length, upper, lower]

def is_contains(string, list_to_search):
    count_calls()  # Подсчитываем вызов функции

    # Проверяем, содержится ли строка в списке без учета регистра
    return any(string.lower() == item.lower() for item in list_to_search)

# Примеры вызова функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Выводим количество вызовов функций
print('Колличество вызовов функции: ', calls)