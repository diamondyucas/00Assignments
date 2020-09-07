# Conditionals

# A Boolean expression is an expression that evaluates to produce a result which is a Boolean value.
# For example, the operator == tests if two values are equal. It produces (or yields) a Boolean value, ex: True
# The float function converts integers and strings to floating-point numbers
# The int function, for example, takes any value and converts it to an integer,
# if possible, or complains otherwise: with value error
# Function calls create a detour in the flow of execution.
# Primary purpose of a return statement: It returns the intended output value computed by a fruitful function
# or it returns the value None for a void function.
# Syntax error: while = 5
# Iteration: The repeated execution of a block of statements is called
# While loops: Loops which repeat a block of code until some condition is no longer met, are known as
# Encapsulation: Taking existing blocks of code and wrapping them into functions is called
# Working in strings: Testing for substrings within a string using the in and not in operators
# Splitting a string with multiple words into a list of individual words
# and Cleaning up your strings to strip off unwanted characters such as tabs and newlines
# Optional parameters: def find(strng, ch, start=0, end=None)
# Strings cannot be changed, only reassigned to new variables which are variations on the original string
# 1.a. Source code- Steps written in a high-level language that a computer will be translated
# and read with a compiler or an interpreter.
# 1.b. Algorithm - is a computer process to solve a problem.
# 1.c. IDE (integrated development environment) - software application that combines a source code edition,
# build automation tools and a debugger to computer programmers.
# 1.d. Interpreter: Program that translates high-level language into a low-level
# language that can be understood by a computer.
# 1.e.Bug - Programming error
# 1.f. Crash: When the computer or program stops working.
# 1.g. Debugger: Program that helps find or fix bugs.
# 1.h. Variable: Something that represents a value.


# 6 common comparison operaters:
# x == y               # Produce True if ... x is equal to y
# x != y               # ... x is not equal to y
# x > y                # ... x is greater than y
# x < y                # ... x is less than y
# x >= y               # ... x is greater than or equal to y
# x <= y               # ... x is less than or equal to y


# Logical operaters
# There are three logical operators, and, or, and not, that allow us to build more complex Boolean
# expressions from simpler Boolean expressions. The semantics (meaning) of these operators is similar
# to their meaning in English. For example, x > 0 and x < 10 produces True only if x is greater than 0
# and at the same time, x is less than 10.
#
# n % 2 == 0 or n % 3 == 0 is True if either of the conditions is True, that is, if the number n is
# divisible by 2 or it is divisible by 3. (What do you think happens if n is divisible by both 2 and
# by 3 at the same time? Will the expression yield True or False? Try it in your Python interpreter.)
#
# Finally, the not operator negates a Boolean value, so not (x > y) is True if (x > y) is False,
# that is, if x is less than or equal to y.
#
# The expression on the left of the or operator is evaluated first: if the result is True,
# Python does not (and need not) evaluate the expression on the right — this is called short-circuit evaluation.
# Similarly, for the and operator, if the expression on the left yields False,
# Python does not evaluate the expression on the right.

# Logical opposites
# operator	logical opposite
# ==	!=
# !=	==
# <	>=
# <=	>
# >	<=
# >=	<