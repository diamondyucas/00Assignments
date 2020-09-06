# Link to book: http://openbookproject.net/thinkcs/python/english3e/index.html
# Link to index: http://openbookproject.net/thinkcs/python/english3e/genindex.html

# My notes

# example of for loop
# for f in ["Jatea","John","Yondez","Tiana","Loren","Marisa","Tianna"]:
    # invite = "Hi " + f + ".  Please come to my party on Saturday!"
    # print(invite)
######################################################################
# example of using turtles

# import turtle
# wn = turtle.Screen()         # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# wn.title("Tess & Alex")

# tess = turtle.Turtle()       # Create tess and set some attributes
# tess.color("hotpink")
# tess.pensize(5)

# alex = turtle.Turtle()       # Create alex

# tess.forward(80)             # Make tess draw equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)               # Complete the triangle

# tess.right(180)              # Turn tess around
# tess.forward(80)             # Move her away from the origin

# alex.forward(50)             # Make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

# wn.mainloop()

# for i in [4]:
    # alex.forward(50)
    # alex.left(90)
#######################################################################
# multicolor square
# import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen")      # Set the window background color
# wn.title("Hello, Tess!")      # Set the window title

# tess = turtle.Turtle()
# tess.color("blue")            # Tell tess to change her color
# tess.pensize(3)               # Tell tess to set her pen width


# for c in ["yellow", "red", "purple", "blue"]:
    # tess.color(c)
    # tess.forward(50)
    # tess.left(90)

# wn.exitonclick
####################################################################
# example of spiral
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.shape("turtle")
# tess.color("blue")

# tess.penup()                # This is new
# size = 20
# for i in range(30):
   # tess.stamp()             # Leave an impression on the canvas
   # size = size + 3          # Increase the size on every iteration
   # tess.forward(size)       # Move tess along
   # tess.right(24)           #  ...  and turn her

# wn.mainloop()
###########################################################################

# Some guidance on the coding portion of the exam: If you’ve been doing the teamwork and homework
# assignments, you should have all the tools in your bag that you need to be successful. You can
# likely expect variables, functions, loops, and conditionals as core concepts of the code. Make
# sure you can identify those concepts in code, refactor them, and create new ones. The tasks we
# give you will NOT be expecting you to be very creative (e.g., “Draw a butterfly!:); instead,
# we want you to implement clearly stated instructions (e.g., “Ask the user to input a number
# between 1 and 10”). If you implement them correctly, :thumbsup:
###################################################################################################
