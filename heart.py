import turtle

pen=turtle.Turtle()

def curve():
    for i in range(200):
        pen.right()
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)

    curve()
    pen.forward(112)
    pen.end_fill()

def txt():
    pen.up()
    pen.setpos(-38, 95)
    pen.down()
    pen.color('orange')
    pen.write("Jamshidharker9363",font=("verdana",12,"bold"))

heart()
txt()
pen.ht()
pen.done()