#Defining Imports
from turtle import*
from random import randint

# Function To Create Turtles
def creating_turtles(color,yCoordinate, rotation):
    turtle = Turtle()
    turtle.color(color)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-160,yCoordinate)
    turtle.right(rotation)
    turtle.pendown()
    return turtle

penup()
speed(10)
goto(-140, 140)

# Printing Dashed Lines
for step in range(15):
    write(step, align='center')
    right(90)
    for step in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

# Calling creating_turtles function
turtle1 = creating_turtles('red',100, 360)
turtle2 = creating_turtles('blue',70, -360)
turtle3 = creating_turtles('green',40, 360)
turtle4 = creating_turtles('purple',10, -360)

# Randomly Moving Turtles
for run in range(100):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))
