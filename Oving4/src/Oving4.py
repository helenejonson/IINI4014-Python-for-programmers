import turtle
import math


# Finding points at circle
def points(dots, radii):
    pointList = []
    for x in range(dots):
        pointList.append(
            [math.sin(x * (2 * math.pi) / dots) * radii, math.cos(x * (2 * math.pi) / dots) * radii])
    return pointList


# Draws a circle without the generator
def draw(pointList, intervals, myTurtle, radii, multi):
    myTurtle.circle(radii)
    myTurtle.penup()
    for x in range(intervals):
        myTurtle.goto(pointList[x])
        myTurtle.pendown()
        point = (x * multi)
        if point > 0:
            if point >= intervals:
                point = point % intervals
            myTurtle.goto(pointList[point])
        myTurtle.penup()


def generator(pointList, multi):
    for x in range(len(pointList)):
        yield x * multi


# Draws with the data from the generator
def drawGen(pointList, intervals, myTurtle, radii, generate):
    myTurtle.circle(radii)
    myTurtle.penup()
    for x, y in zip(pointList, generate):
        myTurtle.goto(x)
        myTurtle.pendown()
        myTurtle.goto(pointList[y % intervals])
        myTurtle.penup()


def main():
    myTurtle = turtle.Turtle()
    w = turtle.Screen()
    myTurtle.speed(0)
    myTurtle.penup()
    myTurtle.goto(0, -200)  # Sets circle in the middle of the screen
    radii = 200
    myTurtle.pendown()
    dots = 150  # number of dots around circle
    multiply = 2  # multiplier
    pointList = points(dots, radii)
    gen = generator(pointList, multiply)

    # Draws without generator
    #draw(pointList, dots, myTurtle, radii, multiply)

    # Draws with generator
    drawGen(pointList, dots, myTurtle, radii, gen)

    w.exitonclick()


main()
