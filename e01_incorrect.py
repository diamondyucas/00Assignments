# What does this function do?
# def is_divisible(x, y):
#      return x % y == 0
# d.
# It divides x by y, and if there is a remainder it returns False.
#
# Question 2
# Which of the following programming constructs would be most appropriate for checking whether a person is old enough to drive?
# c.
# conditional

# Question 3
# True / False: Functions can call other functions.
# The correct answer is 'True'.

# Question 4
# Which of the following programming constructs would be appropriate for summing the numbers from 1 to 100?
# a.
# Loop
#
# Question 5
# Which of the following are Boolean operators?
# The correct answers are: and, not, or
#
# Question 6
# Assuming x is the same, which of the following code blocks produces output that is different from the others?
# for i in [0, 1, 2, 3, 4, 5]:
#    print(i + x)

# Question 7
# If a program (without unit testing) runs once without errors, then the program must be free from _____.
# The correct answer is:
# syntax errors
#
# Question 8

# Programming languages are an example of what type of language?
# The correct answer is:
# Formal Language
#
# Question 9

# True or False: An if statement can include no elif clauses, or as many elif clauses as the developer wants.
# The correct answer is 'True'.

# Question 10
# Match each term to its definition:
# The correct answer is:
# An object of a certain type, or class. → Instance,
# A function that is attached to an object. → Method,
# Causes a loop to stop repeating its body. → Terminating condition,
# Some state or value that belongs to a particular object. → Attribute,
# A template or a blueprint that describes objects of its type → Class
#
# Question 11
# The following line of code uses the indexing operator [ ] . What is the value of n?
#
# n = ____________
# vegetable = "carrot"
# t = vegetable[n]
# print("The letter is ", t)
#
# Output: The letter is a
# The correct answer is: -5
#
# Question 12
# When control exits a function that defines local variables, what happens to the local variables?
# Your answer is correct.
# The correct answer is:
# The local variables are inaccessible because of scope.
#
# Question 13
# The correct order for these items is as follows:
# Checkout the code in PyCharm using "Get from Version Control"
# Create a new branch
# Commit changes to your code
# Merge master into your branch and resolve merge conflicts
# Push your branch to Github
# Issue a pull request

# Question 14
# Which of the following is true about comments?
# The correct answer is:
# The interpreter does not generate machine code for comments.
#
# Question 15
# A software developer mistakenly committed a change which made the software worse. Using git, the developer should _____ the commit.
# The correct answer is:
# revert

# Question 16
# A program should compute 3 multiplied by x. Which of the following statements contains a logic error?
# The correct answer is:
# y = x * x * x
#
# Question 17
# According to the following code, what shape does the turtle t draw?
# for i in range(3):
# t.forward(250)
# t.left(120)
# The correct answer is:
# Triangle
#
# Question 18
# What will a Python interpreter do for the following three lines of code?
# # x = 2 # width
#
# # y = 0.5
#
# # z = x * y total area
# The correct answer is:
# Ignore all three lines
#
# Question 19
# True  or False: A blank commit message is never appropriate.
# The correct answer is 'True'.

# Question 20
# Which of the following loops short circuits?
# The correct answer is:
# for i in range(9):
#     if (i + 1) % 5 == 0:
#         result = i
#         break
# print(result)
#
# Question 21
# Match each definition to the term:
# The correct answer is:
# def = "definition" → syntax error,
# for_while = range(4) → No error,
# x = float(10) / int(0.01) → runtime error,
# def distance(time, speed):
#     ''' Calculate distance by multiplying time by speed '''
#     return time // speed → semantic error,
# turt → token,
# while True:
#     print("Hello world") → infinite loop

# Question 22
# The following function is testable with a test suite from Chapter 6:
# def identity(name):
#     id = input("Enter your id, " + name + ":")
#     return id
# The correct answer is 'False'.

# Question 23
# Which of the following is a valid name for a variable in Python?
# The correct answer is:
# between
#
# Question 24
# Which of the following code follows the best coding practices?
#
# a.
#
# def turn_clockwise(dir):
#     if dir == "N":
#         return "E"
#     elif dir == "E":
#         return "S"
#     elif dir == "S":
#         return "W"
#     elif dir == "W":
#         return "N"
#     else:
#         return "Error"
#
# def main():
#     print(turn_clockwise("S"))
#
# b.
#
# global dir
#
# def turn_clockwise():
#     global dir
#     if dir == "N":
#         return "E"
#     elif dir == "E":
#         return "S"
#     elif dir == "S":
#         return "W"
#     elif dir == "W":
#         return "N"
#     else:
#         return "Error"
#
# def main():
#     global dir
#     dir = "S"
#     print(turn_clockwise())
#
#
# c.
# def turn_clockwise(dir):
#    dir = input("Which direction?")
#    if dir == "N":
#       print("E")
#    elif dir == "E":
#       print("S")
#    elif dir == "S":
#       print("W")
#    elif dir == "W":
#       print("N")
#
# def main():
#    turn_clockwise("S")
#
# d.
# Both a. and c.
#
# Feedback
# Your answer is incorrect.
# The correct answer is:
# def turn_clockwise(dir):
#     if dir == "N":
#         return "E"
#     elif dir == "E":
#         return "S"
#     elif dir == "S":
#         return "W"
#     elif dir == "W":
#         return "N"
#     else:
#         return "Error"
# def main():
#     print(turn_clockwise("S"))

# Question 25
# Which of the following truncates the number 10.5 to 10?
# The correct answer is:
# int()
#
# Question 26
# In an instruction like z = x + y, the symbols x, y, and z are examples of _____.
# The correct answer is:
# variables
#
# Question 27
# Identify the instance of the Turtle class in this code:
# wn = turtle.Screen()
# wn.bgcolor("white")
# turt = turtle.Turtle()
# turt.shape("turtle")
# turt.color("red")
# The correct answer is:
# turt
#
# Question 28
# True or False: None is a String.
# The correct answer is 'False'.

# Question 29
# True or False: The index of the leftmost character of a string is 1.
# The correct answer is 'False'.

# Question 30
# A function square_perimeter(side_length) calculates the perimeter of a square from the length of a side. Which of the following statements correctly tests the function using the testing framework in Teamwork T06?
# The correct answer is:
# testit(40 == square_perimeter(10))

# Question 31
# Which of the following is NOT a reason to use functions in our code?
# The correct answers are:
# It simplifies the order of execution for the interpreter.,
# It limits the scope of local variables to make debugging easier.
#
# Question 32
# Which of the following statements constructs an instance of the Turtle class and assigns it to the variable turt?
# The correct answer is:
# turt = turtle.Turtle()
#
# Question 33
# What type of error will the following line of code produce?
#            print(Hello world!)
# The correct answer is:
# Syntax
#
# Question 34
# True or False: Black box testing a function requires understanding the inputs, outputs, and how the function works.
# The correct answer is 'False'.

# Question 35
# Which of the following is NOT a converter function?
# The correct answer is:
# convert()
#
# Question 36
# Which of the following functions are NOT fruitful function(s)? (select all that apply)
# The correct answers are:
# def fun_1():
#     return None
# ,
# def fun_2():
#    print(None)
# ,
# def fun_7():
#     return
# ,
# def fun_8():
#     pass

# Question 37
# Which of the following functions has unreachable code?
# The correct answer is:
# def absolute_value(x):
#     if x < 0:
#         return -x
#     else:
#         return x
#     return "Error"

# Question 38
# Which of the following techniques involves decomposing a problem into manageable mental chunks?
# The correct answer is:
# Top-Down Design
#
# Question 39
# For a function which takes three integer parameters and returns a single integer value, which of the following statements is true?
# The correct answer is: None of the above

# Question 40
# True or False: The variable num is accessible from the function main().
# The correct answer is 'False'.