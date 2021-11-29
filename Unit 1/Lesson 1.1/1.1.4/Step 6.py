#   a114_divisible.py

# get two numbers from user
num1 = int(input("please enter a number: "))
num2 = int(input("please enter another number: "))
# loop whle the numbers are not divisible (the remainder is 0)
while (num1 % num2 != 0):
    print("num1 is not divisible by num2")
    num1 = int(input("please enter a number: "))
    num2 = int(input("please enter another number: "))
if (num1 % num2 == 0):
  print("num1 is divisible by num2")