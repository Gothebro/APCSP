#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    rem = floor % 9
    if (rem >= 0 and rem <= 2):
        painter.color("gray")
    if (rem > 2 and rem <= 5):
        painter.color("blue")
    if (rem > 5 and rem <= 8 ):
        painter.color("green")
    y = y + 5 # location of next floor
    floor = floor + 1
   
    #draw the floor
    painter.pendown()
    painter.forward(50)
    if (floor % 21 == 0):
        x = x + 60
        y = -150

wn = trtl.Screen()
wn.mainloop()