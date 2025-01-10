def calculate_structure_sum(*args):
    total_sum = 0  # Инициализируем переменную для хранения суммы

    for data in args:  # Проходим по каждому аргументу
        # Проверяем, является ли data списком
        if isinstance(data, list):
            for item in data:  # Проходим по каждому элементу списка
                total_sum += calculate_structure_sum(item)  # Рекурсивно вызываем функцию для каждого элемента
        # Проверяем, является ли data словарём
        elif isinstance(data, dict):
            for key, value in data.items():  # Проходим по каждому ключу и значению
                total_sum += calculate_structure_sum(key)   # Учитываем сумму ключей
                total_sum += calculate_structure_sum(value) # Учитываем сумму значений
        # Проверяем, является ли data кортежем
        elif isinstance(data, tuple):
            for item in data:  # Проходим по каждому элементу кортежа
                total_sum += calculate_structure_sum(item)  # Рекурсивно вызываем функцию для каждого элемента
        # Проверяем, является ли data множеством
        elif isinstance(data, set):
            for item in data:  # Проходим по каждому элементу кортежа
                total_sum += calculate_structure_sum(item)  # Рекурсивно вызываем функцию для каждого элемента
        # Проверяем, является ли data строкой
        elif isinstance(data, str):
            total_sum += len(data)  # Добавляем длину строки к общей сумме
        # Проверяем, является ли data числом (целым или дробным)
        elif isinstance(data, (int, float)):
            total_sum += data  # Добавляем число к общей сумме

    return total_sum  # Возвращаем итоговую сумму

# Пример использования функции
result = calculate_structure_sum([
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
    "Hello",  # Строка
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ])
print(result)