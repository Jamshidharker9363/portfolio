import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(50)
h = 1 
t.pensize(4)
def draw(angle,n):
    t.circle(5+n,60)
    t.left(angle)
    t.circle(5+n,60)
t.goto(0,0)
for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h +=0.005
    t.pencolor(c)
    t.penup()
    draw(90,i)
    draw(180,i)
    t.down()
    draw(1/2,i-i)
    draw(180,i)
    draw(90,i)
t.done()