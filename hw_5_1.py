# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

input_str = input("Введите текст, разделяя слова пробелами: ")
text = 'абв'
input_list = input_str.split()
result_list = []
for t in input_list:
    if text not in t:
        print("Текст без слов, содержащих 'абв': ")
        result_list.append(t)
print("".join(result_list))