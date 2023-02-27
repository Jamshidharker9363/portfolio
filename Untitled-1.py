import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(100)
t.pensize(2)
h = 0.4
t.up()
t.goto(0 ,30)
t.down()
for i in range(260):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.002
    t.color(c)
    t.up()
    t.fd(i*2)
    t.down()
    t.circle(i , -100)
    t.fd(i)
    t.circle(i , -100)

t.done()