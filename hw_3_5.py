# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def neg_fib(k):
    if k>=0:
       x = [0,1]
       for i in range(2, k+1):
           x.append(x[i-1] + x[i-2]) 
       return x[k]
    else:
       k=-k
       x = [1,0]
       for i in range(2, k+2):
           x.append(x[i-2] - x[i-1]) 
       x.reverse()
    return x[0]

k = int(input("Введите целое число:  "))
for i in range(-k,k+1):
    print(neg_fib(i))