#Liam Toebbe
#sept.21.2023
#Unit 1 mosaic assignment

import turtle
turtle.speed(50)
def draw_octagon(side_length):
    for x in range(8):
        turtle.forward(side_length)
        turtle.left(45)
def draw_oct_mosaic(side_length):
    for x in range(8):
        draw_octagon(side_length)
        turtle.left(45)

def draw_pentagon(side_length):
    for x in range (5):
        turtle.forward(50)
        turtle.left(72)
def draw_pent_mosaic(side_length):
    for x in range(10):
        draw_pentagon(side_length)
        turtle.left(36)

def draw_nonagon(side_length):
    for x in range(9):
        turtle.forward(side_length)
        turtle.left(40)
def draw_non_mosaic(side_length):
    for x in range(9):
        draw_nonagon(side_length)
        turtle.left(40)

draw_pent_mosaic(30)

turtle.penup()
turtle.forward(250)
turtle.pendown()

draw_oct_mosaic(30)

turtle.penup()
turtle.backward(500)
turtle.pendown()

draw_non_mosaic(30)

turtle.exitonclick()