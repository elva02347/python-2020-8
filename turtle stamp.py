import turtle
elva = turtle.Turtle()
elva.shape('turtle')
elva.color('sky blue')
elva.penup()
step = 20
for i in range(30):
    elva.forward(step)
    elva.left(24)
    elva.stamp()
    step = step + 3
turtle.done()
