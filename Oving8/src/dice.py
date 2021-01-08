import turtle
import random


class d6:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.pen = turtle.Turtle()
        self.value = 0

    def draw(self):
        w = turtle.Screen()
        self.getValue()
        self.pen.speed(0)
        self.pen.penup()
        self.drawDice()
        self.drawNumber()
        self.pen.goto(0, 0)
        w.exitonclick()

    def getValue(self):
        self.value = random.randint(1, 6)

    def drawDice(self):
        self.pen.fillcolor("red")
        self.pen.pencolor("red")
        self.pen.goto(self.x, self.y)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.forward(self.size)
        self.pen.right(90)
        self.pen.forward(self.size)
        self.pen.right(90)
        self.pen.forward(self.size)
        self.pen.right(90)
        self.pen.forward(self.size)
        self.pen.left(90)
        self.pen.end_fill()
        self.pen.penup()

    def drawNumber(self):
        self.pen.fillcolor("yellow")
        self.pen.pencolor("yellow")
        radii = self.size / 20
        centerx = self.x + self.size / 2
        centery = self.y - self.size / 2
        oneThirdX = self.x + self.size / 3
        oneThirdY = self.y - self.size / 3
        twoThirdX = self.x + self.size - (self.size / 3)
        twoThirdY = self.y - self.size + (self.size / 3)
        if self.value == 1:
            self.one(centerx, centery, radii)
        elif self.value == 2:
            self.two(oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii)
        elif self.value == 3:
            self.one(centerx, centery, radii)
            self.two(oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii)
        elif self.value == 4:
            self.four(oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii)
        elif self.value == 5:
            self.four(oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii)
            self.one(centerx, centery, radii)
        elif self.value == 6:
            self.four(oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii)
            self.six(centery, oneThirdX, twoThirdX, radii)

    def one(self, centerx, centery, radii):
        self.pen.goto(centerx, centery + radii)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radii)
        self.pen.end_fill()
        self.pen.penup()

    def two(self, oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii):
        self.pen.goto(oneThirdX, oneThirdY + radii)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radii)
        self.pen.end_fill()
        self.pen.penup()
        self.pen.goto(twoThirdX, twoThirdY + radii)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radii)
        self.pen.end_fill()
        self.pen.penup()

    def four(self, oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii):
        self.two(oneThirdX, oneThirdY, twoThirdX, twoThirdY, radii)
        self.pen.goto(oneThirdX, twoThirdY + radii)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radii)
        self.pen.end_fill()
        self.pen.penup()
        self.pen.goto(twoThirdX, oneThirdY + radii)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radii)
        self.pen.end_fill()
        self.pen.penup()

    def six(self, centery, oneThirdX, twoThirdX, radii):
        self.pen.goto(oneThirdX, centery + radii)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radii)
        self.pen.end_fill()
        self.pen.penup()
        self.pen.goto(twoThirdX, centery + radii)
        self.pen.begin_fill()
        self.pen.circle(radii)
        self.pen.end_fill()
        self.pen.penup()


if __name__ == "__main__":
    x = input("X position: ")
    y = input("y position: ")
    size = input("Size of dice: ")
    roll = d6(int(x), int(y), int(size))
    # roll = d6(50, 50, 100)
    roll.draw()
