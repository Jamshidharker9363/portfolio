from turtle import*
width(20)
bgcolor('black')
colors = ['#db0f3c','#50ebf7','white']
pos= [(0,0),(-5,13),(-5,5)]

for (x,y),col in zip(pos,colors):
    up()
    goto(x, y)
    down()
    color(col)
    left(180)
    circle(50, 270)
    forward(140)
    left(180)
    circle(50, 90)

    penup()
    goto(-55, -240)
    pendown()
    write("Tik Tok", font=("Microsoft Phagspa",-40, "bold"))

done()