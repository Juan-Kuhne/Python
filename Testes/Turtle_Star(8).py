import turtle as tt

tl = tt.Screen()
st = tt.RawTurtle(tl)
cont = 0
ps = [0, 1, 2, 3, 4, 5, 6, 7]
st.speed(0)
st.width(5)
st.color('yellow', 'red')
st.ht()
st.up()
st.goto(-50, -100)

for i in range(1,9):
    st.fd(60)
    ps[cont] = st.pos()
    # st.write(cont)
    cont += 1
    st.fd(60)
    # st.write(cont)
    st.left(360/8)


print(ps)
st.goto(ps[0])
st.down()
st.begin_fill()
st.goto(ps[6])
st.goto(ps[4])
st.goto(ps[2])
st.goto(ps[0])
st.up()
st.goto(ps[1])
st.down()
st.goto(ps[7])
st.goto(ps[5])
st.goto(ps[3])
st.goto(ps[1])
st.end_fill()
tt.exitonclick()
