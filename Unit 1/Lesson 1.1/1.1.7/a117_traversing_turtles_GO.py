#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)
    t.penup()
    color = turtle_colors.pop()
    t.pencolor(color)

#   sets the starting point variables to the origin
startx = 0
starty = 0
direction = 90
#   sends the turtles to the starting points
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading(direction) 
  t.right(45) 
  t.forward(50)
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()

#   changes the starting variables to up and over fifty 
#   startx = startx + 50
#   starty = starty + 50

wn = trtl.Screen()
wn.mainloop()