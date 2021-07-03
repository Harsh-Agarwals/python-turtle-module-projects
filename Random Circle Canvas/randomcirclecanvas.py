import turtle
import random

colors = ["red", "yellow", "green", "magenta", "lime", "blue", "black", "orange", "purple", "cyan"]


for i in range(50):
    borderColor = random.choice(colors)
    fillColor = random.choice(colors)
    turtle.color(borderColor, fillColor)
    rand1 = random.randint(-300, 300)
    rand2 = random.randint(-300, 300)
    radius = random.randint(1, 51)
    turtle.penup()
    turtle.setpos(rand1, rand2)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.done()
