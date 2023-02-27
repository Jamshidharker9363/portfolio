import turtle
t  = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
col = ('white', 'orange', 'red', 'yellow', 'green', 'blue', 'cyan')
t.speed(0)

for i in range(200):
    t.forward(i*4)
    t.right(91)
    t.color(col[i%7])
    for b in range(3):
        t.forward(i*4)
        t.right(91)
        for c in range(2):
            t.forward(i*4)
            t.right(91)
t.done()            