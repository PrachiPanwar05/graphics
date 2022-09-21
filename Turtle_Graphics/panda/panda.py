import turtle

pen = turtle.Turtle()
def ring(col, rad):
	pen.fillcolor(col)
	pen.begin_fill()
	pen.circle(rad)
	pen.end_fill()

# Draw first ear

pen.up()
pen.setpos(-35, 95)
pen.down
ring('black', 15)

# Draw second ear

pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

# Draw face

pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

# Draw first eye
pen.up()
pen.setpos(-18, 75)
pen.down
ring('black', 8)

# Draw second eye
pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

# Draw first eye
pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

# Draw second eye
pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

##### Draw nose #####
pen.up()
pen.setpos(0, 55)
pen.down
ring('black', 5)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)
pen.hideturtle()
