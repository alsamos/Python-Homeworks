# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число: "))
lst_result = []
res_num = 2
while n > 1:
    if n % res_num == 0:
        lst_result.append(res_num)
        n = n/res_num
    else:
        res_num += 1
print(f'Простые множители числа: {lst_result}')