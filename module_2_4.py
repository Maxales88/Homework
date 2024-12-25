# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебираем каждый элемент из списка numbers
for number in numbers:
    # Предполагаем, что число простое
    is_prime = True

    # Проверяем, является ли число простым
    # Простое число должно быть больше 1
    if number > 1:
        for i in range(2, int(number**0.5) + 1):  # Проверяем делители от 2 до sqrt(number)
            if number % i == 0:  # Если число делится на i без остатка
                is_prime = False  # Число не простое
                break  # Нет смысла продолжать проверку делителей
    else:
        is_prime = False  # Число 1 не простое

    # Записываем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим списки на экран
print("Primes:", primes)
print("Not primes:", not_primes)