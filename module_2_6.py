import random

def generate_pairs():
    # Список для хранения пар чисел, сумма которых равна n
    pairs_with_sum = []

    # Генерация пар чисел от 1 до n
    for i in range(1, n):
        for j in range(i + 1, n):
            if i + j == n:
                pairs_with_sum.append(f"{i}{j}")
    return pairs_with_sum

# Генерация случайного числа от 3 до 20
n = random.randint(3, 20)
print(f'{n} - число из первой вставки')

# Получение пар чисел с искомой суммой для n
pairs = generate_pairs()

print(f'{"".join(pairs)} - нужный пароль')
