# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_enc(in_data):   
	encoding = "" 
	i = 0
	while i < len(in_data):    
		count = 1
		while i + 1 < len(in_data) and in_data[i] == in_data[i + 1]:
			count += 1
			i += 1
		encoding += str(count) + in_data[i]    
		i += 1
	return encoding


def rle_dec(out_data):   
    decoding = ""
    count = ""
    for char in out_data:
        if char.isdigit():    
            count += char
        else:                
            decoding += char * int(count) 
            count = "" 
    return decoding

       
def read_data(file):   
    with open(str(file), "r", encoding="UTF-8") as data:
        input_string = data.read()
    return input_string



init_text = "C:\\Users\\Asus\\Downloads\\GeekBrains\\Python\\init_text.txt"  
print(read_data(init_text)) 
en_text = "C:\\Users\\Asus\\Downloads\\GeekBrains\\Python\\en_text.txt"    
print(rle_enc(read_data(init_text))) 
with open(str(en_text), "w", encoding="UTF-8") as data:
    data.write(rle_enc(read_data(init_text)))
dec_text = "C:\\Users\\Asus\\Downloads\\GeekBrains\\Python\\dec_text.txt" 
print(rle_dec(read_data(en_text)))   
with open(str(dec_text), "w", encoding="UTF-8") as data:
    data.write(rle_dec(read_data(en_text)))