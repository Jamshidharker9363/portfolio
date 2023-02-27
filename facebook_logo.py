import turtle
from turtle import*

wn = Screen()
t= turtle.Turtle()

t.color("#2272f2")
t.begin_fill()
t.circle(140, 360)
t.end_fill()





t.right(7)
t.backward(32)
t.color('white')
t.begin_fill()
t.left(97)
t.forward(90)
t.left(90)
t.forward(48)
t.right(90)
t.forward(40)
t.right(90)
t.forward(48)
t.left(90)
t.forward(34)
t.circle(-45, 90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(20)
t.circle(17, 90)
t.forward(23)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(108)
t.right(90)
t.forward(48)
t.right(90)
t.forward(8)
t.end_fill()
t.hideturtle()


def go (x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

t.pencolor('#2272f2')
t.fillcolor('#2272f2')
t.pensize(30)

go(-45, -120)
t.seth(50)
t.forward(100)
t.circle(-50, 90)
t.circle(-120, 60)
t.circle(-30, 130)
t.forward(160)
t.circle(50, 90)
t.circle(120, 60)
t.circle(32, 130)
t.forward(50)

t.penup()
t.goto(-55, -240)
t.pendown()
t.pencolor('black')
t.write("Meta", font=("Microsoft Phagspa",40, "bold"))


turtle.done()