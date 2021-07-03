import turtle


def circle(col, rad):
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()


turtle.up()
turtle.setpos(-35, 95)
turtle.down()
circle('black', 15)

turtle.up()
turtle.setpos(35, 95)
turtle.down()
circle('black', 15)

turtle.up()
turtle.setpos(0, 60)
turtle.down()
circle('white', 35)

turtle.up()
turtle.setpos(-15, 93)
turtle.down()
circle('black', 7)

turtle.up()
turtle.setpos(15, 93)
turtle.down()
circle('black', 7)

turtle.up()
turtle.setpos(-15, 93)
turtle.down()
circle('white', 4)

turtle.up()
turtle.setpos(15, 93)
turtle.down()
circle('white', 4)

turtle.up()
turtle.setpos(0, 80)
turtle.down()
circle('black', 6)

turtle.right(90)
turtle.up()
turtle.setpos(0, 80)
turtle.down()
turtle.circle(5, 180)

turtle.up()
turtle.setpos(0, 80)
# turtle.right(90)
turtle.down()
turtle.circle(5, -180)

turtle.penup()
turtle.done()
