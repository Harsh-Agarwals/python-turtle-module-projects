import turtle

color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
turtle.bgcolor('black')
for x in range(360):
    turtle.pencolor(color[x % 6])
    turtle.width(x/100 + 1)
    turtle.forward(x)
    turtle.left(59)
turtle.done()
