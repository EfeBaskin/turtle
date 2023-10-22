"""
#polygon
turtle1=turtle.Turtle()
numSides=5
angle=360/numSides
side_length=100
for i in range(numSides):
    turtle1.right(angle)
    turtle1.forward(side_length)
turtle.done()
"""

#shrinking squares

import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("python turtle")

colors_turtle = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle_instance = turtle.Turtle()
turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    turtle_instance.pencolor(colors_turtle[i % 6])
    turtle_instance.width(i // 100 + 1)
    turtle_instance.forward(i)
    turtle_instance.left(60)

#turtle.done()
turtle.mainloop()




