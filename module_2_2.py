first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))

# создаем условие равенства всех вводимых чисел
if first == second and second == third:
    print(3)

# дополняем условие равенства хотябы двух вводимых чисел
elif first == second or second == third or first == third:
    print(2)

# при невыполнении двух вышеуказанных условий вводимые числа не будут равны по определению
else:
    print(0)
