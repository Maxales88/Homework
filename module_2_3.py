my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0  # Начальный индекс для прохождения по списку
while index < len(my_list):  # Цикл для перебора элементов списка
    number = my_list[index]  # Создаем переменную для печати чисел из списка
    if number < 0:  # Проверка на отрицание
        break  # Если встречается отрицательное число, прерывается цикл
    if number > 0:  # Условие вывода на печать только положильных чисел, без нуля
        print(number)  # Печатаем положительне число
    index += 1  # Переход к следующему элементу

