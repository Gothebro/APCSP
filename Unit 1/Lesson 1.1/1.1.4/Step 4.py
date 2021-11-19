#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Add a loop with a zero-iteration condition
non0 = 5
while (non0 < 5):
    painter.circle(200)
# Add an infinite loop
zero = 0
while (zero > -1):
    painter.circle(50,360,22)
    painter.forward(1)
    painter.right(20)
    zero = zero + 1

wn = trtl.Screen()
wn.mainloop()