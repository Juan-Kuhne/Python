import turtle as tt

tl = tt.Screen()
st = tt.RawTurtle(tl)
st.ht()
st.width(5)
st.color('red', 'yellow')
st.speed(0)
cont = 0
ps = [0, 1, 2, 3, 4, 5]
st.up()
st.goto(-60, -(207.85/2))
for i in range(1,7):
    st.fd(60)
    #st.write(cont)
    ps[cont] = st.pos()
    cont += 1
    st.fd(60)
    st.left(60)

#print(ps)
st.goto(ps[5])
st.down()
st.begin_fill()
st.goto(ps[1])
st.goto(ps[3])
st.goto(ps[5])
st.up()
st.goto(ps[0])
st.down()
st.goto(ps[4])
st.goto(ps[2])
st.goto(ps[0])
st.end_fill()

tt.exitonclick()
