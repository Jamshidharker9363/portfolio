import turtle
from turtle import *

t=turtle.Turtle()
wn=Screen()

wn=bgcolor("black")
t.pensize(22)

#
t.setposition(0,-260)
t.pendown()
t.begin_fill()
t.color("orange")
t.pencolor("white")
t.circle(250)
t.end_fill()
t.penup()

#
t.pensize(2)
t.setposition(0,-220)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(210)
t.penup()


t.setposition(38,-110)
t.pendown()
t.begin_fill()
t.color("orange")
t.pensize(10)
t.pencolor("white")
t.forward(20)
t.backward(100)
t.left(60)
t.backward(100)
t.right(60)
t.backward(100)
t.right(117)
t.backward(700)
t.right(63)
t.backward(90)
t.right(90)
t.backward(470)
t.right(90)
t.backward(95)
t.right(90)
t.backward(40)
t.end_fill()
t.penup()


t.pensize(10)
t.setposition(52,-32)
t.pendown()
t.begin_fill()
t.color("black")
t.pencolor("white")
t.right(90)
t.forward(85)
t.right(115)
t.forward(220)
t.right(155)
t.forward(198)
t.end_fill()


t.backward(40)
t.left(46)
t.forward(118)
t.right(94)
t.forward(118)
t.hideturtle()

turtle.done()