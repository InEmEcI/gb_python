# 4 Показать первую цифру дробной части числа.

num = float(input("Введите дробное число: "))  # 5.77

round_num = int(num)  # 5

result = (num - round_num) * 10  # 7.7

print(f' первая цифра дробной части: {int(result)}')