# Functions

# a function is a named sequence of statements that belong together. Their primary purpose
# is to help us organize programs into chunks that match how we think about the problem.

# example of syntax for a function
# def NAME( PARAMETERS ):
    # STATEMENTS

# If the first thing after the function header is a string, it is treated as a
# docstring and gets special treatment in Python
# Docstrings are usually formed using triple-quoted strings as they allow us to
# easily expand the docstring later on should we want to write more than a one-liner.
# Use: they just need to know what arguments our function takes, what it does, and what the expected result is.
# When we create a local variable inside a function, it only exists inside the function, and we cannot use it outside.
# function call - A statement that executes a function. It consists of the name of the function
# followed by a list of arguments enclosed in parentheses.
# argument - A value provided to a function when the function is called. This value is
# assigned to the corresponding parameter in the function. The argument can be the result
# of an expression which may involve operators, operands and calls to other fruitful functions.
# refactor - A fancy word to describe reorganizing our program code, usually to make it more understandable.

# rectangle
# def draw_rectangle(t, w, h):
    # """Get turtle t to draw a rectangle of width w and height h."""
    # for i in range(2):
        # t.forward(w)
        # t.left(90)
        # t.forward(h)
        # t.left(90)

# Purpose of functions
# Creating a new function gives us an opportunity to name a group of statements.
# Functions can simplify a program by hiding a complex computation behind a single command.
# The function (including its name) can capture our mental chunking, or abstraction, of the problem.
# Creating a new function can make a program smaller by eliminating repetitive code.

# Example of fruitful function
# Where:
# P = principal amount (initial investment)
# r = annual nominal interest rate (as a decimal)
# n = number of times the interest is compounded per year
# t = number of years
# def final_amt(p, r, n, t):
#     """
#       Apply the compound interest formula to p
#        to produce the final amount.
#     """
#
#     a = p * (1 + r/n) ** (n*t)
#     return a         # This is new, and makes the function fruitful.
#
# # now that we have the function above, let us call it.
# toInvest = float(input("How much do you want to invest?"))
# fnl = final_amt(toInvest, 0.08, 12, 5)
# print("At the end of the period you'll have", fnl)
# The return statement is followed an expression (a in this case).
# This expression will be evaluated and returned to the caller as the “fruit” of calling this function.


# print(Hello world!)
