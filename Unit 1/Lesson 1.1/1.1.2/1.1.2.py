# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
# create sketch
painter.circle(50, 360, 6)
painter.right(120)
painter.circle(50, 360, 6)
painter.left(240)
painter.circle(50, 360, 6)
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()

