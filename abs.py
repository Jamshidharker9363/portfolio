import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(10)
h = 0.1
for i in range(280):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.01
    t.pencolor(c)
    t.left(120)
    t.circle(i-60,180)
    t.left(120)
t.done()