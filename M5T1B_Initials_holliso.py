#CTI-110
#M5T1b - Initials
#Oliver Hollis
#22-10-2017

import turtle
wn = turtle.Screen()
t = turtle.Turtle()
turtle.hideturtle()

def main():
# A blue Turtle
    t.pencolor('blue')

# size of turtle nib
    t.pensize(5)    

# Draw a letter "H"
    t.left(90)
    t.forward (100)
    t.back (50)
    t.right(90)
    t.forward (40)
    t.left (90)
    t.forward (50)
    t.back (100)

# Move Turtle to left
    t.penup()
    t.left(90)
    t.forward(70)
    t.right(90)
    t.forward(50)
    t.pendown()

    t.pencolor('green')

# Draw a letter "O"
    t.circle(50)
main()
    

    








