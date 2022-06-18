from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()
tim.speed('fast')


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def down():
    tim.backward(10)


def up():
    tim.forward(10)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key='w', fun=up)
screen.onkey(key='a', fun=left)
screen.onkey(key='d', fun=right)
screen.onkey(key='s', fun=down)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
