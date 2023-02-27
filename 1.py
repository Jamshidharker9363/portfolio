import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(1000)
h = 0
for i in range(905):
    c =colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(c)
    t.rt(i)
    t.circle(125, i )
    t.fd(i)
    t.rt(90)
    t.fd(i)
    t.rt(90)

t.done()