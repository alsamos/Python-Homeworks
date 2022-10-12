# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def man_man(swts_move, swts_total):
    while swts_total > 2 * swts_move:
        first_player = int(input(f"Игрок 1, сколько конфет хотите забрать (1 - {swts_move})? "))
        if first_player <= 0 or first_player > swts_move:    
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.") 
            break
        else:
            swts_total = swts_total - first_player
        second_player = int(input(f"Игрок 2, сколько конфет хотите забрать (1 - {swts_move})? "))
        if second_player <= 0 or second_player > swts_move:
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.")
            break
        else: 
            swts_total = swts_total - second_player
            print(f"1й игрок - {first_player} конфет, 2й игрок - {second_player} конфет, остаток - {swts_total}")
    while swts_total <= 2 * swts_move:
        first_player = int(input(f"Игрок 1, сколько конфет хотите забрать (1 - {swts_move})? "))
        if first_player <= 0 or first_player > swts_move:
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.")
            break
        else: 
            swts_total = swts_total - first_player
            print(f"1й игрок - {first_player} конфет, остаток - {swts_total}")
            if swts_total <= swts_move:    
                    print(f"Остаток {swts_total} <= количества конфет, которые можно взять за 1 ход. Победил 2й игрок") 
                    exit()   
        second_player = int(input(f"Игрок 2, сколько конфет хотите забрать (1 - {swts_move})? "))
        if second_player <= 0 or second_player > swts_move:
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.")
            break
        else: 
            swts_total = swts_total - second_player
            print(f"2й игрок - {second_player} конфет, остаток - {swts_total}")
            if swts_total <= swts_move:
                print(f"Остаток {swts_total} <= количества конфет, которые можно взять за 1 ход. Победил 1й игрок")
                exit() 


def man_bot(swts_move, swts_total):
    while swts_total > 2 * swts_move:
        first_player = int(input(f"Игрок 1, сколько конфет хотите забрать (1 - {swts_move})? "))
        if first_player <= 0 or first_player > swts_move:    
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.") 
            break
        else:
            swts_total = swts_total - first_player
        second_player = random.randint(1, swts_move)
        print("Игрок 2: ", second_player)
        swts_total = swts_total - second_player
        print(f"1й игрок - {first_player} конфет, 2й игрок - {second_player} конфет, остаток - {swts_total}")
    while swts_total <= 2 * swts_move:
        first_player = int(input(f"Игрок 1, сколько конфет хотите забрать (1 - {swts_move})? "))
        if first_player <= 0 or first_player > swts_move:
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.")
        else: 
            swts_total = swts_total - first_player
            print(f"1й игрок - {first_player} конфет, остаток - {swts_total}")
            if swts_total <= swts_move:    
                    print(f"Остаток {swts_total} <= количества конфет, которые можно взять за 1 ход. Победил 2й игрок") 
                    exit()   
        second_player = random.randint(1, swts_move)
        print("Игрок 2: ", second_player)
        swts_total = swts_total - second_player
        print(f"2й игрок - {second_player} конфет, остаток - {swts_total}")
        if swts_total <= swts_move:
            print(f"Остаток {swts_total} <= количества конфет, которые можно взять за 1 ход. Победил 1й игрок")
            exit() 
                            

def man_ii(swts_move, swts_total):
    while swts_total > 2 * swts_move:
        first_player = int(input(f"Игрок 1, сколько конфет хотите забрать (1 - {swts_move})? "))
        if first_player <= 0 or first_player > swts_move:    
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.") 
            break
        else:
            swts_total = swts_total - first_player
        second_player = swts_total % (swts_move + 1)
        if second_player == 0:
            second_player == 1
        print("Игрок 2: ", second_player)
        swts_total = swts_total - second_player
        print(f"1й игрок - {first_player} конфет, 2й игрок - {second_player} конфет, остаток - {swts_total}")
    while swts_total <= 2 * swts_move:
        first_player = int(input(f"Игрок 1, сколько конфет хотите забрать (1 - {swts_move})? "))
        if first_player <= 0 or first_player > swts_move:
            print(f"За 1 ход можно взять от 1 до {swts_move} конфет. Начните заново.")
        else: 
            swts_total = swts_total - first_player
            print(f"1й игрок - {first_player} конфет, остаток - {swts_total}")
            if swts_total <= swts_move:    
                    print(f"Остаток {swts_total} <= количества конфет, которые можно взять за 1 ход. Победил 2й игрок") 
                    exit()   
        second_player = swts_total % (swts_move + 1)
        if second_player == 0:
            second_player == 1
        print("Игрок 2: ", second_player)
        swts_total = swts_total - second_player
        print(f"2й игрок - {second_player} конфет, остаток - {swts_total}")
        if swts_total <= swts_move:
            print(f"Остаток {swts_total} <= количества конфет, которые можно взять за 1 ход. Победил 1й игрок")
            exit()     



sweets = int(input("Введите суммарное количество конфет в игре: "))
per_move = int(input("Введите число конфет, которые можно забрать за 1 ход, но не более суммарного количества конфет в игре:  "))
if sweets <= per_move or sweets <= 0 or per_move <= 0: print("При таких вводных игра не имеет смысла. Перечитайте правила и попробуйте снова.")
who = int (input("Выберите, с кем играть. Нажмите 1 для 'с другим игроком', 2 для 'с ботом', 3 для 'с умным ботом': "))
if who == 1: man_man(per_move, sweets)
if who == 2: man_bot(per_move, sweets)
if who == 3: man_ii(per_move, sweets)
if who <1 or who > 3: print("Нет соперника под таким номером. Повторите попытку.")