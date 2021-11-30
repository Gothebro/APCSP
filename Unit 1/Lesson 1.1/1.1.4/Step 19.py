#   a114_nested_loops_4.py 
import turtle as trtl
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
painter.speed(0)
x = -200
y = 0
move_x = 1
move_y = 1

while (x < 100):
  
  while (y < 100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1
  
  while (y > 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1

x = -200
y = 0
painter.penup()
painter.goto(x,y)
painter.pendown()
move_x = 1
move_y = -1

while (x < 100):
  while (y > -100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1
  
  while (y < 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1

wn = trtl.Screen()
wn.mainloop()