#CTI-110
#M5T1A - Shapes
#Oliver Hollis
#22-10-2017


import turtle
wn = turtle.Screen()
t = turtle.Turtle()
turtle.hideturtle()

# A red Turtle for trinagle
t.pencolor('red')    

# size of turtle nib
t.pensize(5)    

# Draw a triangle
def main():
    t.forward(70)             
    t.left(120)
    t.forward(70)
    t.left(120)
    t.forward(70)
    t.left(120)


# Move Turtle 
    t.penup()
    t.left(-210)
    t.forward(40)
    t.right(60)
    t.pendown()

# A green Turtle for square
    t.pencolor('green')

# Draw a square
    t.forward(60)            
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)

main()
