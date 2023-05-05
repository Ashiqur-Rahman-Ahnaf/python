import turtle as t
import colorsys as c
t.setup(450,600)
t.speed(0)
t.tracer(10)
t.width(3)
t.bgcolor("black")
for j in range(20):
    for i in range(10):
        t.color(c.hsv_to_rgb(i/10,j/20,1))
        t.right(90)
        t.circle(150-j*4,90)
        t.left(90)
        t.circle(150-j*4,90)
        t.right(180)
        t.forward(20)
        t.right(160)
        t.circle(60,20)
t.hideturtle()
t.done()