# Создайте программу для игры в ""Крестики-нолики"".

def create_playground(b):   
    for i in range(3): 
        print(b[0 + i * 3], b[1 + i * 3], b[2 + i * 3])


def make_move(x_o):  
    valid = False
    while not valid:
        move = input("Укажите, куда поставить " + x_o + ":")
        try:
            move = int(move)
        except:
            print(f"Некорректный ввод. Вы уверены, что ввели число от {1} до {9} ? ")
            continue
        if move >= 4 and move <= 6:
            if (str(playground[move - 1]) not in "XO"):
                playground[move - 1] = x_o
                valid = True
            else: 
                print("Эта клетка уже занята!")
        elif move >= 1 and move <= 3:
            if (str(playground[move + 5]) not in "XO"):
                playground[move + 5] = x_o
                valid = True
            else: 
                print("Эта клетка уже занята!")
        elif move >= 7 and move <= 9:
            if (str(playground[move - 7]) not in "XO"):
                playground[move - 7] = x_o
                valid = True
            else: 
                print("Эта клетка уже занята!")        
        else: 
            print("Некорректный ввод. Введите число от 1 до 9")


def check_win(b):   
    winner_combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    win = ""
    for i in winner_combinations:
        if b[i[0]] == "X" and b[i[1]] == "X" and b[i[2]] == "X":
            win = "X"
        if b[i[0]] == "O" and b[i[1]] == "O" and b[i[2]] == "O":
            win = "O"         
    return win
 

def the_game(b):
    for i in range(4):
        create_playground(b)
        make_move("X")
        check = check_win(b)
        if check: 
            print("\n" + check, "выиграл!")
            create_playground(b)
            exit()
        create_playground(b)
        make_move("O")
        check = check_win(b)
        if check: 
            print("\n" + check, "выиграл!")
            create_playground(b)
            exit()
    i = i + 1
    create_playground(b)
    make_move("X")
    check = check_win(b)
    if check: 
        print("\n" + check, "выиграл!")
        create_playground(b)
        exit()
    else:
        print("Ничья!")
        create_playground(b)
        exit()

playground = [7,8,9,4,5,6,1,2,3]
the_game(playground)