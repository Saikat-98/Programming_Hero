# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
	for i in range(50):
		pen.right(4)
		pen.forward(4)

# Defining method to draw a full heart
def heart():

	pen.fillcolor('red')

	pen.begin_fill()

	pen.left(140)
	pen.forward(113)

	curve()
	pen.left(120)

	curve()

	pen.forward(112)

	pen.end_fill()

# Defining method to write text
def txt():

	pen.up()

	pen.setpos(-68, 95)

	pen.down()

	pen.color('lightyellow')

	pen.write("        Coding", font=("Verdana", 12, "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()

turtle.done()
