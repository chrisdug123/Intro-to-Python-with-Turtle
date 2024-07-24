# """
# This is the Template Repl for Python with Turtle.

# Python with Turtle lets you make graphics easily in Python.

# Check out the official docs here: https://docs.python.org/3/library/turtle.html
# """

# import turtle

# # Fullscreen the canvas
# screen = turtle.Screen()
# screen.setup(1.0, 1.0)

# # Begin!
# t = turtle.Turtle()

# for c in ['red', 'green', 'blue', 'yellow']:
#   t.color(c)
#   t.forward(75)
#   t.left(90)

# screen.mainloop()

from turtle import *
import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)
t = turtle.Turtle()
for i in range(4):
  t.forward(50)
  t.right(90)

screen.mainloop()
