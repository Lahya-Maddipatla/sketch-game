from turtle import *
t=Turtle()
def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
def move_left():
    t.setheading(t.heading()+10)
def move_right():
    t.setheading(t.heading()-10)
def clear():
    t.clear()
    t.penup()
    t.goto(0,0)

s=Screen()
s.listen()
s.onkey(move_forward,"w")
s.onkey(move_backward,"s")
s.onkey(move_left,"a")
s.onkey(move_right,"d")
s.onkey(clear,"c")
s.title("Etch sketch")
s.exitonclick()