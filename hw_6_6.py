# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# lst = [2, 3, 5, 6, -1, 10]
# print(lst)
# mult = 0
# if not len(lst)%2:
#     for i in range(0, len(lst)//2):
#         mult = lst[i] * lst[-i-1]
#         print(mult)
# else:
#     for i in range(0, len(lst)//2+1):
#         mult = lst[i] * lst[-i-1]
#         print(mult)

# LIST COMPREHENSION

lst = [2, 3, 5, 6, -1, 10]
print(lst)
mult = 0
mult = [(lst[i] * lst[-i-1]) for i in range(0, (len(lst)//2)) if not len(lst)%2]
print(mult)
if len(lst)%2:
    mult = [(lst[i] * lst[-i-1]) for i in range(0, len(lst)//2+1)]        
    print(mult)