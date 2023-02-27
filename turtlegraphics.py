import turtle
import colorsys
t= turtle.Turtle()
turtle.bgcolor('black')
t.pencolor('gray')
t.speed(0)
t.width(3)
h=0
for i in range(180):
    c=colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    t.forward(250)
    t.right(-33)
    t.circle(80,130)
    t.right(10)
    t.forward(100)
    t.penup()
    t.speed(0)
    t.backward(100)
    t.right(-10)
    t.circle(80,-130)
    t.right(35)
    t.backward(250)
    t.right(2)
    t.pendown()
    h+=0.011
turtle.done()