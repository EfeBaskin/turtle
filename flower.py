import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('brown')
rotate=int(90)
def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size-=6
def mission1(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(400/repeat)
mission1(s,200,10)
t1 = turtle.Turtle()
t1.speed(0)
t1.color('yellow')
rotate=int(90)
def Circles1(t,size):
    for i in range(6):
        t.circle(size)
        size=size-10
def mission2(t,size,repeat):
    for i in range (repeat):
        Circles1(t,size)
        t.right(400/repeat)
mission2(t1,160,10)
t2= turtle.Turtle()
t2.speed(0)
t2.color('light blue')
rotate=int(80)
def Circles2(t,size):
    for i in range(4):
        t.circle(size)
        size-=10
def mission3(t,size,repeat):
    for i in range (repeat):
        Circles2(t,size)
        t.right(400/repeat)
mission3(t2,120,10)
t3 = turtle.Turtle()
t3.speed(0)
t3.color('pink')
rotate=int(90)
def Circles4(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def mission4(t,size,repeat):
    for i in range (repeat):
        Circles4(t,size)
        t.right(400/repeat)
mission4(t3,80,10)
t4= turtle.Turtle()
t4.speed(0)
t4.color('green')

rotate=int(90)
def Circles5(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def mission5(t,size,repeat):
    for i in range (repeat):
        Circles5(t,size)
        t.right(400/repeat)
mission5(t4,40,10)
turtle.done()