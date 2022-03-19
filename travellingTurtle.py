from turtle import Turtle, Screen
count = 4
squirtle = Turtle()
squirtle.shape("turtle")
squirtle.color("aquamarine")
squirtle.forward(150)
squirtle.right(90)
squirtle.forward(150)
squirtle.right(90)
squirtle.forward(300)
squirtle.right(90)
squirtle.forward(150)
squirtle.right(90)
squirtle.forward(150)
while count > 0:
    squirtle.forward(150)
    squirtle.left(90)
    count -= 1

screen = Screen()
screen.exitonclick()
