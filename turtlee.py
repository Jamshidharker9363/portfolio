import turtle as t
import colorsys as col
t.bgcolor('black')
t.tracer(25)
t.ht()
h = 0.04
t.penup()
t.goto(-150, -150)
t.down()
for i in range(150):
  c = col.hsv_to_rgb(h, 1 ,1)
  h += 0.005
  t.color(c)
  t.begin_fill()
  t.fd(i)
  t.rt(91)
  t.up()
  t.circle(150-i, 90)
  t.down()
  t.circle(150-i, 90)
  t.end_fill()

t.done()