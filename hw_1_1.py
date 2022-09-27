# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Введите цифру, обозначающую день недели, от 1 до 7:  "))
if a>0 and a<6: 
    print(f"{a}й день недели не является выходным")
elif a==6 or a==7:
    print(f"{a}й день недели является выходным")
else: 
    print(f"число {a} вне диапазона [1-7]")