import turtle
import time
from random import randint

score = 0
#Title
t=turtle.Pen()
t.pencolor("Blue")
t.hideturtle()
t.penup()
t.setposition(-150,350)
t.write("Catch The Turtle Game", font=("Verdana", 18))


#Set up screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Catch the Turtle")

#for border
mypen = turtle.Turtle()
mypen.penup()
mypen.speed("fastest")
mypen.hideturtle()
mypen.setposition(-300,-300)
mypen.pendown()
for side in range(4):
    mypen.color("red")
    mypen.forward(300)
    mypen.color("black")
    mypen.forward(300)
    mypen.left(90)
    mypen.hideturtle()

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("blue")
score_turtle.penup()
score_turtle.goto(400, 150)
score_turtle.write("Score: 0".format(score), font=("Verdana", 25))

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.turtlesize(2)
player.penup()

start = time.time()
def game_turtle():

   while time.time()-start<40:
        player.hideturtle()
        time.sleep(2)
        player.setposition(randint(-250, 200),randint(-250, 200))
        player.showturtle()
        time.sleep(0.5)

        def on_click(x, y):
            global score
            score += 1
            score_turtle.clear()
            score_turtle.write(f"Score: {score}",font=("Verdana", 25))

        player.onclick(on_click)

game_turtle()












turtle.mainloop()
