# # Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# # Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
 
def wr_file(st):
    with open('record.txt', 'w') as data:
        data.write(st)
 
def cr_lst(k):
    lst = []
    for i in range(k + 1):
        lst.append(randint(0, 101))    
    return lst
    
def cr_polynom(sp):
    lst = sp[::-1]
    polyn = ''
    if len(lst) < 1:
        polyn = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                polyn += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst [i + 1] != 0:
                    polyn += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                polyn += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    polyn += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                polyn += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                polyn += ' = 0'
    return polyn
 

k = int(input('Введите натуральную степень k:  '))

deg = cr_lst(k)
wr_file(cr_polynom(deg))

print('Результат выполнения задачи записан в файл record.txt')