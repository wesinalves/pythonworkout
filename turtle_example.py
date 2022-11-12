import turtle
from random import uniform

def setup():
    """ Provide the config for the screen """
    turtle.title('Multiple Squares Animation')
    turtle.setup(300, 300, 100, 100)
    turtle.speed(1)
    turtle.hideturtle()


def draw_square(size):
    """ Draw a square in the current direction """
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

def draw_lines(x, s):
    turtle.setx(x)
    turtle.sety(0)
    turtle.forward(s)

setup()
# for _ in range(0, 12):
#     draw_square(50)
#     # Rotate the starting direction
#     turtle.right(120)
turtle.left(90)
for i in range(0, 12):
    draw_lines(i * 10, uniform(0,100))

# Add this so that the window will close when clicked on
turtle.exitonclick()
