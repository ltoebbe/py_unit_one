import turtle
turtle.speed(1000**1000)
for x in range(360):
    turtle.left(1)
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
turtle.exitonclick()