# Сообщить в какой четверти координатной плоскости
# или на какой оси находится точка с координатами Х и У.

x = int(input('Введите X: '))
y = int(input('Введите Y: '))
# Вариант 1
# if (x > 0) and (y > 0): print('I четверть')
# if (x < 0) and (y > 0): print('II четверть')
# if (x < 0) and (y < 0): print('III четверть')
# if (x > 0) and (y < 0): print('IV четверть')
# if (x == 0) and (y == 0): print('в начале координат')

# Вариант 2
def quarter(x, y):
    print([['I', 'II'], ['IV', 'III']][y < 0][x < 0], 'четверть')
quarter(x, y)