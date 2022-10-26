import turtle
from turtle import *
from random import randint

screen =  turtle.Screen()
t = turtle.Turtle()
speed(0)

t.penup()
t.goto(-325,225)
t.pendown()

t.color("green")
t.begin_fill()
t.forward(625)
t.right(90)
t.forward(450)
t.right(90)
t.forward(625)
t.right(90)
t.forward(450)
t.end_fill()

t.penup()
t.goto(-300,0)
t.pendown()


t.color("yellow")
t.begin_fill()
t.right(55)
t.forward(350)
t.right(70)
t.forward(350)
t.right(110)
t.forward(350)
t.right(70)
t.forward(350)
t.end_fill()


t.penup()
t.goto(-100,-120)
t.pendown()

t.color("blue")
t.begin_fill()
for i in range(360):
    t.right(1)
    t.forward(2.5)    

t.end_fill()


t.penup()
t.goto(-150,50)
t.pendown()
t.right(140)

t.color("white")
t.begin_fill()
for i in range(99):
    t.right(0.5)
    t.forward(3)
t.right(65)
for i in range(8):
    t.right(1)
    t.forward(2.5)
t.right(105)
for i in range(98):
    t.left(0.5)
    t.forward(3)
t.right(105)

for i in range(10):
    t.right(1)
    t.forward(2.5)

t.end_fill()

def draw_star(length):
    angle = 150
    side = length
    pointies = 5
    ROTATION = 360/pointies

    angle_left = angle
    angle_right = angle

    t.color("white")
    t.begin_fill()
    for p in range(pointies):
        t.forward(side)
        t.right(angle_right)
        t.forward(side)
        t.left(angle_left)
        t.right(ROTATION)
    t.end_fill()

t.penup()
t.goto(40,40)
t.pendown()
draw_star(7)

def has_colision(points, x, y):    
    for point in points:
        if (abs(point['x'] - x) < 5 and abs(point['y'] - y) < 5):
            return True
        else:
            return False

points = []
for i in range(23):
    position = False
    colision = False
    while position is False:
        x = randint(-100, 100)
        y = randint(-100, 0)
        if x < 80 and y < -20:
            colision = has_colision(points, x, y)
            if colision is True:
                points.pop()
            else:
                points.append({'x': x, 'y': y})
                position = True
            
    t.penup()
    t.goto(x,y)
    t.pendown()    
    draw_star(randint(3, 7))
turtle.done()
