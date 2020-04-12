from turtle import *
from math import sqrt

tamLet = 10
Re = 's'

def xPlayer(x, y):
    up()
    pencolor('blue')
    goto(x, y)
    seth(90)
    forward(40)
    left(90)
    forward(40)
    left(135)
    down()
    forward(sqrt(12800))
    left(135)
    up()
    forward(80)
    left(135)
    down()
    forward(sqrt(12800))

def oPlayer(x, y):
    up()
    pencolor('red')
    goto(x, y)
    fillcolor('white')
    seth(270)
    forward(40)
    left(90)
    down()
    begin_fill()
    circle(40)
    end_fill()
    
def fim(ply):
    up()
    goto(0, -200)
    text = 'Jogador "{}" ganhou!!!'.format(ply)
    write(text, align = "center", font = ('Arial', 12, 'bold'))

def board():
    speed(0)
    ht()
    width(8)
    up()
    goto(-50, -150)
    left(90)
    down()
    forward(300)
    up()
    goto(50, -150)
    down()
    forward(300)
    up()
    goto(-150, -50)
    right(90)
    down()
    forward(300)
    up()
    goto(150, 50)
    left(180)
    down()
    forward(300)
    up()
    pencolor('green')
    goto(-100, 100 - tamLet)
    write('1', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(0, 100 - tamLet)
    write('2', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(100, 100 - tamLet)
    write('3', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(-100, 0 - tamLet)
    write('4', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(0, 0 - tamLet)
    write('5', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(100, 0 - tamLet)
    write('6', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(-100, -100 - tamLet)
    write('7', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(0, -100 - tamLet)
    write('8', align = 'center', font = ('Arial', tamLet, 'normal'))
    goto(100, -100 - tamLet)
    write('9', align = 'center', font = ('Arial', tamLet, 'normal'))


Screen()
while(True):
    board()
    use = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win = ''

    for i in range(1, 10):
        if i % 2 == 1:
            op = numinput('jogador X', 'Digite uma posição', minval = 1, maxval = 9)
            if op == 1:
                xPlayer(-100, 100)
                use[0] = 'x'
            if op == 2:
                xPlayer(0, 100)
                use[1] = 'x'
            if op == 3:
                xPlayer(100, 100)
                use[2] = 'x'
            if op == 4:
                xPlayer(-100, 0)
                use[3] = 'x'
            if op == 5:
                xPlayer(0, 0)
                use[4] = 'x'
            if op == 6:
                xPlayer(100, 0)
                use[5] = 'x'
            if op == 7:
                xPlayer(-100, -100)
                use[6] = 'x'
            if op == 8:
                xPlayer(0, -100)
                use[7] = 'x'
            if op == 9:
                xPlayer(100, -100)
                use[8] = 'x'
        else:
            op = numinput('jogador O', 'Digite uma posição', minval = 1, maxval = 9)
            if op == 1:
                oPlayer(-100, 100)
                use[0] = 'o'
            if op == 2:
                oPlayer(0, 100)
                use[1] = 'o'
            if op == 3:
                oPlayer(100, 100)
                use[2] = 'o'
            if op == 4:
                oPlayer(-100, 0)
                use[3] = 'o'
            if op == 5:
                oPlayer(0, 0)
                use[4] = 'o'
            if op == 6:
                oPlayer(100, 0)
                use[5] = 'o'
            if op == 7:
                oPlayer(-100, -100)
                use[6] = 'o'
            if op == 8:
                oPlayer(0, -100)
                use[7] = 'o'
            if op == 9:
                oPlayer(100, -100)
                use[8] = 'o'

        if use[0] == 'x' and use[1] == 'x' and use[2] == 'x' or use[3] == 'x' and use[4] == 'x' and use[5] == 'x' or use[6] == 'x' and use[7] == 'x' and use[8] == 'x' or use[0] == 'x' and use[3] == 'x' and use[6] == 'x' or use[1] == 'x' and use[4] == 'x' and use[7] == 'x' or use[2] == 'x' and use[5] == 'x' and use[8] == 'x' or use[0] == 'x' and use[4] == 'x' and use[8] == 'x' or use[2] == 'x' and use[4] == 'x' and use[6] == 'x':
            win = 'X'
            break
        elif use[0] == 'o' and use[1] == 'o' and use[2] == 'o' or use[3] == 'o' and use[4] == 'o' and use[5] == 'o' or use[6] == 'o' and use[7] == 'o' and use[8] == 'o' or use[0] == 'o' and use[3] == 'o' and use[6] == 'o' or use[1] == 'o' and use[4] == 'o' and use[7] == 'o' or use[2] == 'o' and use[5] == 'o' and use[8] == 'o' or use[0] == 'o' and use[4] == 'o' and use[8] == 'o' or use[2] == 'o' and use[4] == 'o' and use[6] == 'o':
            win = 'O'
            break

    up()
    goto(0, -200)
    down()
    if win == 'X' or win == 'O':
        write('Jogador "{}" Ganhou'.format(win), align = 'center', font = ('Arial', 15, 'normal'))
    else:
        pencolor('black')
        write('Empate'.format(win), align = 'center', font = ('Arial', 15, 'normal'))
		
    Re = textinput('Jogador "{}" Ganhou!'.format(win) ,'Deseja jogar novamente? s/n')
    
    if Re == 'n':
        break
    clearscreen()
