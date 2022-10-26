"""
Import Turtle
Make Turtle Object
Define a method to draw a curve with simple forward and left moves
Define a method to draw the full heart
- virar a esquerda
- andar para frente
- desenhar a curva
- desenhar outra curva
- andar para frente
fill the red color in it
Define a method to display some text by setting position
Call all the methods in main section.
"""


# Import turtle package
import turtle

# Creating a turtle object(donatelo)
donatelo = turtle.Turtle()

# Defining a method to draw curve
def curve(steps=200):
	sentinel = 0
	while sentinel < steps:
		# Defining step by step curve motion
		donatelo.right(1)
		donatelo.forward(1)
		sentinel += 1

# Defining method to draw a full heart
def heart():

	# Set the fill color to red
	donatelo.fillcolor('red')

	# Start filling the color
	donatelo.begin_fill()

	# Draw the left line
	donatelo.left(140)
	donatelo.forward(113)

	# Draw the left curve
	curve()
	donatelo.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	donatelo.forward(112)

	# Ending the filling of the color
	donatelo.end_fill()

# Defining method to write text
def txt():

	# Move turtle to air
	donatelo.up()

	# Move turtle to a given position
	donatelo.setpos(-68, 95)

	# Move the turtle to the ground
	donatelo.down()

	# Set the text color to lightblue
	donatelo.color('white')

	# Write the specified text in
	# specified font style and size
	donatelo.write("Evelyn e Wesin", font=(
	"Verdana", 12, "bold"))
	

def main():
	# Draw a heart
	heart()

	# Write text
	txt()

	# To hide turtle
	donatelo.ht()
	turtle.exitonclick()

main()
