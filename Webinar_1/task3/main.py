
# Вывести на экран числа от -N до N.

num = int(input('Введите челое число: '))

def printNum(number):
    number = abs(number)
    first = number * -1
    sec = number
    while first <= sec:
        print(f'{first},', end="")
        first += 1

printNum(num)