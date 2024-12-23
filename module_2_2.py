first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

# создаем условие равенства всех вводимых чисел
if first == second and second == third:
    print(3)

# дополняем условие равенства хотябы двух вводимых чисел
elif first == second or second == third or first == third:
    print(2)

# при невыполнении двух вышеуказанных условий вводимые числа не будут равны по определению
else:
    print(0)
