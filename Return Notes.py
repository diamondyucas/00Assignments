# Return Statements

# Reason why we use return statements is for when we want a function to return a value

# Function for returning a cubed number

# def #cube(num):
    # return num*num*num

# print (cube(3))

# use if statements only if the answer can be true or false
# use else if statements to input another condition

# Function for printing each letter

# for letter in "Dimond Yucas":
    # print(letter)

# Function for loop using range

# friends = ["Jatea", "Yondez", "John"]

# for index in range(5):
    # print(friends[index])

# len(str): finds the length of a string
# str[i]: the subscript operation extracts the i’th character of the string, as a new string
# str[i:j]: the slice operation extracts a substring out of a string
# str.find(target): returns the index where target occurs within the string, or -1 if it is not found

# Boolean operaters: and, or, not

# What does function return
# fruit = "banana"
# m = fruit[3]
# print(m)

# Returns a

import turtle
wn = turtle.Screen()
t = turtle.Turtle()

for i in range(3):
    t.forward(250)
    t.left(120)

wn.exitonclick()