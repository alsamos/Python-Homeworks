# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

# n = int(input("Введите число:  "))
# lst = []
# sm = 0
# for i in range(1, n+1):
#     j = round((1+1/i)**i, 2)
#     sm +=j
#     lst.append(str(j))
# print(", ".join(lst))
# print(sm)

# ENUMERATE:

n = int(input("Введите число:  "))
lst = []
sm = 0
for i in range(1, n+1):
    j = round((1+1/i)**i, 2)
    sm +=j
    lst.append(str(j))
print(list(enumerate(lst)))
print(sm)