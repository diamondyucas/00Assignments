# ####################################################################################
# # Author:
# # Username:
# #
# # Assignment: E1 - Coding Portion
# # Purpose: Evaluate your ability to write code in Python
# # Value: 25 points total
# #
# # Instructions:
# #   Complete ALL of the tasks indicated below. Read carefully!
# #   Even if you do not complete all tasks, submit what you complete before the class period ends.
# #   Anything pushed after the class end time will not be considered while grading.
# #   You may use the Python documentation, your own code, any code we've given you as part of this class,
# #       and the online book. No other resources, especially no Googling!
# #   You must do this alone without a partner and without help from your classmates.
# #
# # Overview:
# #   This program draws a lovely array of autumn-colored leaves.
# #
# ####################################################################################
# #
# # TODO A successful student will have completed the following tasks:
# #   Task 1: Refactor the code to use a main() function. (6 pts)
# #   Task 2: Ask the user to input a number between 1 and 4.  (3 pts)
# #   Task 3: Call the draw_autumn function, indicating how many leaves to draw using the user's input from Task 2. (4 pts)
# #   Task 4: Fix the draw_autumn() function by converting it to use a loop and iterate the right number of times. (8 pts)
# #   Task 5: Add docstrings and comments where appropriate, modify this header, and clean up any unused code. (4 pts)
# #   Bonus: Include a new function that writes "It's September" to the turtle screen.
# #          modify main() to use this new function correctly if the user picked four. (+3 pts)
#
# ####################################################################################
# # Submission Instructions:
# # Use git to commit and push your changes to the GitHub repository.
# # Make sure your push is complete before the end of class!
# ####################################################################################
#
# import turtle
#
#
# def draw_diamond(t, angle, c, lgth):
#     """
#     This function draws a rounded diamond. DO NOT MODIFY!!!
#
#     :param t: A turtle for drawing.
#     :param angle: An angle that the turtle should initially face.
#     :param c: A color with which to fill the ellipse.
#     :param lgth: length of the long side of the ellipse
#     :return: None
#     """
#     t.color(c)
#     t.begin_fill()
#     t.setheading(angle + 25)
#     radius = 50
#     for loop in range(2):               # Draws 2 halves of ellipse
#         t.circle(radius*4*lgth, 90, 2)  # One half
#         t.circle(radius/4, 90, 2)       # ... and the other half
#     t.end_fill()
#
#
# def draw_leaf(t, color):
#     """
#     Draws a single leaf.     DO NOT MODIFY!!!
#
#     :param t: a turtle object
#     :param color: the color of the leaf
#     :return: None
#     """
#
#     # draws the leaf body
#     draw_diamond(t, 30 * 0, color, 1)       # little leaf part
#     draw_diamond(t, 30 * 1.5, color, 1.5)   # big leaf part
#     draw_diamond(t, 30 * 3, color, 1)       # little leaf part
#
#     # draws the stem
#     t.pensize(20)
#     t.color("brown")
#     t.left(180)
#     t.pendown()
#     t.forward(200)
#     t.circle(400, 15, 2)
#
#
# def move_leaf(t):
#     '''
#     Moves the leaf 125 pixels to the right. DO NOT MODIFY!!!
#
#     :param t: a turtle object
#     :return: None
#     '''
#     t.penup()
#     t.setheading(0)
#     t.goto(t.xcor(), 0)
#     t.forward((40))
#     t.pendown()
#
#
# def colors(col):
#     """
#     Returns a color. DO NOT MODIFY!!!
#
#     :param col: color number
#     :return: String representing a color
#     """
#     if col == 0:
#         return "sienna"
#     elif col == 1:
#         return "orange"
#     elif col == 2:
#         return "darkred"
#     elif col == 3:
#         return "darkorange"
#
#
# def draw_autumn(t, leaves):
#     """
#     # Draws leaves in program
#     :param t: a turtle object
#     :param leaves: creates 4 leaves
#     :return: None
#     """
#
#     # Draws four leaves
#     for i in range(leaves):
#         draw_leaf(t, colors(i % 4))
#         move_leaf(t)
#
#
# def main():
#     t = turtle.Turtle()
#     w = turtle.Screen()
#     t.speed(8)
#     t.penup()
#     t.setpos(-300, 0)
#     t.pendown()
#     user_input = input("Please enter a number between 1 and 4: ")
#     convert = int(user_input)
#     draw_autumn(t, convert)
#     w.exitonclick()
#
#
# main()