def get_matrix(n, m, value):
    # Проверка на неотрицательное значение аргумента
    if n <= 0 or m <= 0:
        return ['Недействительное значение аргумента функции!']

    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для строк
    for i in range(n):
        # Создаем пустой список для каждой строки
        row = []

        # Внутренний цикл для столбцов
        for j in range(m):
            # Заполням список значениями value
            row.append(value)

        # Добавляем список в матрицу
        matrix.append(row)
    # Возвращаем созданную матрицу
    return  matrix

# Пример использования функции
result1 = get_matrix(3, 4, 10 )
print(result1)
print('------->')

result2 = get_matrix(4, 5, 46)
print(result2)
print('------->')

result3 = get_matrix(5, 6, 32)
print(result3)
print('------->')

result4 = get_matrix(0, 8, 32)
print(result4)
print('------->')

result = get_matrix(7, 7, 7)
print("Матрица 7x7, заполненная 7:")
for k in result:
    print(k)
