def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина str_number больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Берем первую цифру и преобразуем ее в число
        first = int(str_number[0])

        # Проверка: если первая цифра не равна 0, перемножаем
        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            # Если первая цифра 0, просто вызываем функцию с оставшимися цифрами
            return get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина str_number равна 1, проверяем цифру и возвращаем 1 для 0
        return int(str_number) if str_number != '0' else 1


# Проверим работу функции
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Вывод: 24

