import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
t.pensize(2)
h =0
for i in range(300):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    h += 0.006

    t.right(119)
    t.circle(-i*0.3,120)
    t.circle(i*0.3,120)
    t.circle(-i*0.3,90)
    t.circle(i*0.3,90)
t.done()