from random import *
import time 


def user_borders_check(lnum, rnum):      #проверяем что границы - являются числами
    return lnum.isdigit() and rnum.isdigit()

def is_valid(num):       #проверяем введенный ответ на корректность
    return (num.isdigit() and int(lnum) <= int(num) <= int(rnum))


def start_game():
    list_1 = 'Ваше число больше загаданного, попробуйте еще разок'
    list_2 = 'Ваше число меньше загаданного, попробуйте еще разок'
    list_win = 'Вы угадали, поздравляем!'    
    print('Введите левую границу промежутка')
    global lnum
    lnum = input()
    time.sleep(0.5)
    print('Введите правую границу промежутка')
    global rnum
    rnum = input()
    while user_borders_check(lnum, rnum) == False:
        print('А может быть все-таки введем корректные числа?')
        lnum = input()
        rnum = input()      
    
    if int(lnum) > int(rnum):
        lnum, rnum = rnum, lnum
        num_for_user = randint(int(lnum), int(rnum))
        print(f'Введите ваше число от {lnum} до {rnum}')
    else:
        num_for_user = randint(int(lnum), int(rnum))
        print(f'Введите ваше число от {lnum} до {rnum}')    
        
    
    counter = 0
    while True:
        num_of_user = input()
        if is_valid(num_of_user) == False:
            print('1А может быть все-таки введем корректные числа?')
        else:
            num = int(num_of_user)
            if num > num_for_user:
                print(list_1)
                print("Введите Другое число")
                counter += 1
                continue
            elif num < num_for_user:
                print(list_2)
                print("Введите другое число")
                counter += 1
                continue
            else: 
                print(list_win,"Количество попыток =", counter+1)
                print('Сыграем еще раз? Введите "да" или "нет"')
                answer = input()
                if answer in ['да','lf']:
                    start_game()
                else:
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    break
                

#Приглашение в игру
print("ИГРА - Числовая угадайка!")
time.sleep(0.5)
print('Сыграешь со мной? Введите "да" или "нет"')
answer = input().lower()
if answer in ['да','lf']:
    print("Правила Игры:")
    time.sleep(0.5)
    print("Компьютер загадывает число в промежутке числе, который вы задаете.", "Ваша задача отгадать это число за минимальное количество попыток!", sep = '\n')
    time.sleep(0.5)
    start_game()
else:
    print('До свидания, мой друг!')
    

