import turtle as t
import colorsys

from cool import draw
t.bgcolor('black')
t.tracer(200)
h = 1
t.pensize(4)
def darw(angle,n):
    t.circle(30+n,90)
    t.left(angle)
    t.circle(30+n,n)
t.goto(-30,0)
for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 0.008
    t.pencolor(c)
    draw(60,i)
    draw(90,i)
    draw(120,i)
t.done()