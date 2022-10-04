# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

lst = [4.1, 2.05, 3.007, 4.18, 5.29]
print(lst)
lst_frac = []
for i in range(len(lst)):
    lst_frac.append(round(math.fmod(lst[i], 1.0),3))
print(lst_frac)
min = lst_frac[0]
max = lst_frac[1]
for i in range(len(lst_frac)):
    if lst_frac[i] < min: 
        min = lst_frac[i]
    if lst_frac[i] > max:
        max = lst_frac[i]
sum = min + max
print(round(sum,3))