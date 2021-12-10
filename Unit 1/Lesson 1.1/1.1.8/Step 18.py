#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 50:
  for t in horiz_turtles:
    t.forward(8)
  for t in vert_turtles:
    t.forward(8)
  
  for h in horiz_turtles:
    for v in vert_turtles:
      xDistance = abs(h.xcor()-v.xcor())
      yDistance = abs(h.ycor()-v.ycor())
      if xDistance < 20:
        if yDistance < 20:
          horiz_turtles.remove(h)
          vert_turtles.remove(v)


wn = trtl.Screen()
wn.mainloop()
