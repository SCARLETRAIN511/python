import turtle
wn=turtle.Screen()
wn.bgcolor('lightgreen')

tess=turtle.Turtle()
tess.pensize(5)
distance=100
angle=180-36
for i in range(5):
    tess.forward(distance)
    tess.left(angle)


wn.exitonclick()