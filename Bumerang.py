import turtle
import colorsys
turtle.Screen().bgcolor("black")
t = turtle.Pen()
t.speed(11)
c = [colorsys.hsv_to_rgb(h*0.3,1,0.9) for h in range(6)]
for i in range(500):
    t.pencolor(c[i%5])
    t.width(i/100 + 1)
    t.pu()
    t.forward(i*2)
    t.left(269*3.14+80)
    t.pd()
    t.circle(i,80)
    t.right(3.14*44+69)
    t.forward(10)
    t.circle(i,10)
turtle.done()
