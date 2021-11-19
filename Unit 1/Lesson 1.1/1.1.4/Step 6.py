#   a114_divisible.py

# get two numbers from user

# loop whle the numbers are not divisible (the remainder is 0)

  # inform user of result 
  
  # gather user input again
  
# inform user of result 
num1 = int(input("please enter a number: "))
num2 = int(input("please enter another number: "))

while (num1 % num2 != 0):
    print("num1 is not divisible by num2")
    num1 = int(input("please enter a number: "))
    num2 = int(input("please enter another number: "))