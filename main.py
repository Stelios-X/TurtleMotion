import turtle

t = turtle.Turtle()


# Creating a staircase...


def myturtle():
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(90)

    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)


n = 3
for i in range(0, n):
    myturtle()

turtle.done()
