import turtle 
screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(10)
color = ['green','yellow','blue','cyan']
c = 0
for i in range(80):
  t.forward(i*7)
  t.right(144)
  t.color(color[c])
  if c==0:
      c=0
  else:
        c+=1

turtle.done()