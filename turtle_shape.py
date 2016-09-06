import turtle as t
import math
import random

x = 30
colors = ["red","orange","yellow","green","blue","indigo","violet"]
t.speed(1000)

def shape(sides, color):
    # put the pen down
    t.pendown()
    # give our shape a color!
    t.begin_fill()
    t.fillcolor(color)

    # draw the square (with a loop!)
    for x in range(sides):
        t.forward(50/math.log(sides))
        t.right(360/sides)
    t.end_fill()
    t.penup()
    t.forward(50)

for i in range(20):
    for j in range(x):
        shape((j + 3), colors[random.randint(0,(len(colors)-1))])
        t.right(360/(10+j))
    t.home()
    t.right(20*(i+1))
t.exitonclick()
