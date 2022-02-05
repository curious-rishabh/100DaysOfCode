import turtle

from matplotlib import colors

colors = ['red', 'blue', 'green','yellow','orange','purple']

turtle.bgcolor('black')
turtle.speed(0)
# 0 means maximum speed

for i in range(360):
    turtle.pencolor(colors[i%6])
    turtle.width(i/100 +1)
    turtle.forward(i)
    turtle.left(59)

turtle.done()
