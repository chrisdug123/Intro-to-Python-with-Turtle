# # """
# # This is the Template Repl for Python with Turtle.

# # Python with Turtle lets you make graphics easily in Python.

# # Check out the official docs here: https://docs.python.org/3/library/turtle.html
# # """

# # import turtle

# # # Fullscreen the canvas
# # screen = turtle.Screen()
# # screen.setup(1.0, 1.0)

# # # Begin!
# # t = turtle.Turtle()

# # for c in ['red', 'green', 'blue', 'yellow']:
# #   t.color(c)
# #   t.forward(75)
# #   t.left(90)

# # screen.mainloop()

# from turtle import *
# import turtle

# screen = turtle.Screen()
# screen.setup(1.0, 1.0)
# t = turtle.Turtle()
# # for i in range(4):
# #   t.forward(50)
# #   t.right(90)

# # t.color('#0866ff')
# # t.circle(50)
# # t.color('white')
# # t.forward(100)
# # t.color('red')
# # t.circle(50)
# # t.begin_fill()
# # t.circle(50)
# # t.end_fill()

# bgcolor("yellow")
# t.hideturtle()
# t.circle(50)
# t.penup()
# t.forward(100)
# t.pendown()
# t.circle(50)
# t.showturtle()

# screen.mainloop()
from turtle import *
import turtle
t=turtle.Turtle()
screen = turtle.Screen()
screen.setup(1.0, 1.0)

planetColour=["Orange","Grey","Red","Green"]
planetSize=[60,20,40,30]
planetDistance=[100,80,90,0]

for i in range (4):
  t.color(planetColour[i])
  t.begin_fill()
  t.circle(planetSize[i])
  t.end_fill()
  t.penup()
  t.forward(planetDistance[i])

screen.mainloop()
