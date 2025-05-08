#!/usr/bin/env python

print("hello world")

# This is how we take notes on our code, so that our notes are right next to our code.

"""
This is a multi-line comment.
It can span multiple lines without issues.
It's also commonly used to write documentation within your code.
Some documentation systems actually parse multi-line comments to generate nice docs.
"""

# y = mx + b
# y = 3x + 1

x = 5
y = 3 * x + 1
print(y)

name = "Beegimus Maximus"
print(name)

print(name + " is cool")
print(5 + x)

# 1 is an integer
# "bobby" is a string ---- string is a "string" of "characters"
# 0.5 if a floating point number, also called "float"
# True and False are booleans -- the capitalization does matter
# There is also None

# print("hello" + 1) breaks
# print(1 + None) breaks
# print(True + "hello") breaks
print(1 + True)
# The above works because it converts True to 1
print(1 + 0.5)
# integers and floats are compatible

def add(a, b):
    return a + b

print(add(2, 3))

# Homework: Define a function named subtract. You can guess how it should work.
# Call that function with the inputs 10 and 7, and print the output.
