#CTI-110
#M5T1C - Snowflake
#Oliver Hollis
#22-10-2017


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

# different colors
color = ["cyan", "purple", "red"]

def main():
    def branch():
        for i in range(4):
            for i in range(3):
                t.forward(30)
                t.backward(30)
                t.right(45)
            t.left(90)
            t.backward(30)
            t.left(45)
        t.right(90)
        t.forward(40)
        t.color(random.choice(color))

    for i in range(11): 
        branch()
        t.left(23)  # I used wierd angles for fun
    
main()        
  
