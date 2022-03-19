import random
from turtle import Turtle, Screen


def randomTravel():
    distance = random.randint(20, 50)
    squirtle.forward(distance)


def randomTurn():
    angle = random.randint(45, 90)
    direction = random.randint(0, 1)
    if direction == 0:
        squirtle.left(angle)
    else:
        squirtle.right(angle)


count = random.randint(10, 20)


squirtle = Turtle()
squirtle.color("aquamarine")

while count > 0:
    randomTravel()
    randomTurn()
    count -= 1


screen = Screen()
screen.exitonclick()
