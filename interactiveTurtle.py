import turtle
drawing_table = turtle.Screen()
drawing_table.bgcolor("grey")
drawing_table.title("interactive board")
myTurtle = turtle.Turtle()
drawing_table.listen()
def forward():
    myTurtle.forward(100)

def rotate_left():
    myTurtle.left(100)
def rotate_right():
    myTurtle.right(100)

def clear_screen():
    myTurtle.clear()

def return_home():
    myTurtle.home()
def pen_up():
    myTurtle.penup()
def pen_down():
    myTurtle.pendown()
drawing_table.onkey(fun= forward, key= "space" )
drawing_table.onkey(fun= rotate_left, key= "Left" )
drawing_table.onkey(fun= rotate_right, key= "Right" )
drawing_table.onkey(fun= clear_screen, key= "c")
drawing_table.onkey(fun= return_home, key= "m")
drawing_table.onkey(fun= pen_up, key= "q")
drawing_table.onkey(fun= pen_down, key= "w")
drawing_table.exitonclick()
turtle.done()

