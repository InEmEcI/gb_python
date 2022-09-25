# 6 Дано число обозначающее день недели. Вывести его название и
# указать является ли он выходным.


def days(num):
    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'субота', 'воскресение']
    if num < 1 or num > 7:
        print('вы ввели не коректное значение')
    elif num >= 6:
        print(f' {week[num - 1]} это выходной день')
    else:
        print(f' {week[num - 1]} это рабочий день')


number = int(input("Введите день недели: "))
days(number)