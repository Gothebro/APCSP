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
looper = 0
while (looper < num_legs):
    spider.goto(0,20)
    spider.setheading(heading*looper)
    spider.forward(leg_length)
    looper = looper + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()