import turtle

turtle_screen = turtle.Screen()

turtle_screen.bgcolor("black")

turtle_screen.title("spiral helix drawing")

turtle_instance = turtle.Turtle()

colorList = ["yellow","blue","red","orange","grey"]

turtle.speed(0)

turtle.Pen()

for i in range(10):
    turtle_instance.color(colorList[i % 5])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(5)

turtle.done()