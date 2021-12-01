#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
num_legs = 6
leg_length = 70
heading = 380 / num_legs
spider.pensize(5)
looper = 0
while (looper < num_legs):
    spider.goto(0,0)
    spider.setheading(heading*looper)
    spider.forward(leg_length)
    looper = looper + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()