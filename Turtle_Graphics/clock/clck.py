import turtle
screen = turtle.Screen()
screen.setup(500, 500)
clk = turtle.Turtle()
clk.color('Green')
clk.width(4)

def draw_hour_hand():
	clk.penup()
	clk.home()
	clk.right(90)
	clk.pendown()
	clk.forward(100)

val = 0
for i in range(12):
	val += 1
	clk.penup()
	clk.setheading(-30 * (i + 3) + 75)
	clk.forward(22)
	clk.pendown()
	clk.forward(15)
	clk.penup()
	clk.forward(20)
	clk.write(str(val), align="center",
			font=("Arial",
					12, "normal"))

clk.setpos(2, -112)
clk.pendown()
clk.width(2)
clk.fillcolor('Green')
clk.begin_fill()
clk.circle(5)
clk.end_fill()

clk.penup()
draw_hour_hand()
clk.setpos(-20, -64)
clk.pendown()
clk.penup()

clk.setpos(-30, -170)
clk.pendown()
clk.write('Clock', font=("Arial", 14,
							"normal"))
clk.hideturtle()
turtle.done()
