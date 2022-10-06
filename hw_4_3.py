# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Вариант 1

lst = [1, 8, 5, 4, 4, 7, 65, 2, 5, 6]
print(lst)
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)

# Вариант 2 (по возрастанию значений)

# import numpy

# lst = [1, 8, 5, 4, 4, 7, 65, 2, 5, 6]
# print(lst)
# unique = numpy.unique(lst)
# print(unique)