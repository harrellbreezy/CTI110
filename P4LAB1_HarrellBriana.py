# Briana Harrell 
# December 13 2025
# P4LAB1
# This program draws a colorful house using Python turtle graphics

import turtle

screen = turtle.Screen()
screen.bgcolor("pink")

# Create turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

side = 150

# Draw square
t.color("black", "yellow") 
t.begin_fill()
for i in range(4):
    t.forward(side)
    t.left(90)
t.end_fill()


t.left(90)
t.forward(side)
t.right(90)

# Draw triangle
t.color("black", "lightblue")
t.begin_fill()

count = 0
while count < 3:
    t.forward(side)
    t.left(120)
    count += 1

t.end_fill()

t.hideturtle()
screen.mainloop()
