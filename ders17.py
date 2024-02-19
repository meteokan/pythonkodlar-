import turtle
a=turtle.Turtle()
b=turtle.Turtle()
a.color("red")
a.penup()
a.back(50)
a.pendown()
for i in range(4):
    a.forward(100)
    a.left(90)
b.back(250)
for j in range(3):
    b.forward(100)
    b.left(120)


turtle.done()