#CTI-110
#M5LAB - Snowflake
#Oliver Hollis
#25-10-2017


import turtle
import random
wn = turtle.Screen()
t = turtle.Turtle()
turtle.hideturtle()

# Move Turtle 
t.penup()
t.forward(90)
t.left(45)
t.pendown()


def main():
    def branch():
        for i in range(3):
            for i in range(3):
                t.forward(30)
                t.backward(30)
                t.right(45)
            t.left(90)
            t.backward(30)
            t.left(45)
        t.right(90)
        t.forward(90)
        

    for i in range(8): 
        branch()
        t.left(45) 
    
main() ()
