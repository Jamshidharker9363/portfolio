from turtle import *
import colorsys
import turtle
speed(0)
bgcolor('black')
h=0.5
pensize(3)
for i in range(300):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.005
    fd(i*3)
    lt(39)
    for j in range(2):
        lt(20)
        rt(39)
    rt(120)
turtle.done()