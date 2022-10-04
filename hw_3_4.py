# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num_dec = int(input("Введите целое десятичное число: "))
num_bin = ' '
while num_dec > 0:
    num_bin = str(num_dec % 2) + num_bin
    num_dec = num_dec // 2
print(num_bin)

# ИЛИ

# num_dec = int(input("Введите целое десятичное число: "))
# num_bin = print(bin(num_dec))

#:)

