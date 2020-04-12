import turtle as tt

tela = tt.Screen()
seta = tt.RawTurtle(tela)
seta.speed(0)
seta.ht()
seta.up()
cont = 0
ps = [0, 1, 2, 3, 4, 5]
while True:
    ps[cont] = seta.pos()
    cont += 1
    seta.fd(150)    
    seta.lt(72)
    if abs(seta.pos()) <1:
        break

seta.width(5)
seta.color('orange', 'yellow')
seta.down()
seta.begin_fill()
seta.goto(ps[3])
seta.goto(ps[1])
seta.goto(ps[4])
seta.goto(ps[2])
seta.goto(ps[0])
seta.end_fill()

print(ps)
tt.exitonclick()
