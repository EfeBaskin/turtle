import turtle

turtle_screen = turtle.Screen()

turtle_screen.bgcolor("light green")

turtle_screen.title("turtle python")

turtle_instance = turtle.Turtle()

turtle_instance.color("red")

def shrinkingSquares(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size -= 20
shrinkingSquares(150)
shrinkingSquares(140)
shrinkingSquares(130)
shrinkingSquares(120)
shrinkingSquares(110)
shrinkingSquares(100)
shrinkingSquares(90)
shrinkingSquares(80)
shrinkingSquares(70)
shrinkingSquares(60)

turtle.done()