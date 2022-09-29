# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input("Введите число:  "))
str_num = str(num)
str_num = str_num.replace('.', '')
lst_num = list(str_num)
lst_num = map(int, lst_num)
result = sum(lst_num)
print(result)