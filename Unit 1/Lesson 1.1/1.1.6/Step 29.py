#   a116_buggy_image.py
import turtle as trtl

# creates spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# configure spider legs
num_legs = 8
leg_length = 70
heading = 360 / num_legs
spider.pensize(5)

# draws spider legs
legs_drawn = 0
while (legs_drawn < num_legs):
    spider.goto(0,20)
    spider.setheading(heading*legs_drawn)
    spider.forward(leg_length)
    legs_drawn = legs_drawn + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()