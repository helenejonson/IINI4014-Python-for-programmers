import random as r
import turtle


class Die:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        pen = turtle.Turtle()
        win = turtle.Screen()
        self.drawSquare(pen)
        rand = r.randint(1, 6)
        radii = (self.size / 10) * 0.75
        if rand == 1:
            self.drawOne(pen, radii)
        elif rand == 2:
            self.drawTwo(pen, radii)
        elif rand == 3:
            self.drawOne(pen, radii)
            self.drawTwo(pen, radii)
        elif rand == 4:
            self.drawFour(pen, radii)
        elif rand == 5:
            self.drawFour(pen, radii)
            self.drawOne(pen, radii)
        else:
            self.drawFour(pen, radii)
            self.drawSix(pen, radii)
        win.exitonclick()

    def drawSquare(self, pen):
        pen.up()
        pen.goto(self.x, self.y)
        pen.down()
        pen.fillcolor("blue")
        pen.begin_fill()
        for x in range(4):
            pen.forward(self.size)
            pen.left(90)
        pen.end_fill()

    def drawOne(self, pen, radii):
        pen.up()
        pen.goto(self.x + (self.size / 2), self.y + (self.size / 2) - radii)
        pen.down()
        pen.fillcolor("black")
        pen.begin_fill()
        pen.circle(radii)
        pen.end_fill()

    def drawTwo(self, pen, radii):
        pen.up()
        first = self.size / 6
        second = 5 * (self.size / 6)
        for x in range(2):
            if x == 0:
                pen.goto(self.x + first, (self.y + second) - radii)
            else:
                pen.goto(self.x + second, (self.y + first) - radii)
            pen.down()
            pen.fillcolor("black")
            pen.begin_fill()
            pen.circle(radii)
            pen.end_fill()
            pen.up()

    def drawFour(self, pen, radii):
        pen.up()
        self.drawTwo(pen, radii)
        first = self.size / 6
        second = 5 * (self.size / 6)
        for x in range(2):
            if x == 0:
                pen.goto(self.x + first, (self.y + first) - radii)
            else:
                pen.goto(self.x + second, (self.y + second) - radii)
            pen.down()
            pen.fillcolor("black")
            pen.begin_fill()
            pen.circle(radii)
            pen.end_fill()
            pen.up()

    def drawSix(self, pen, radii):
        pen.up()
        first = self.size / 6
        second = 5 * (self.size / 6)
        for x in range(2):
            if x == 0:
                pen.goto(self.x + first, (self.y + (self.size / 2)) - radii)
            else:
                pen.goto(self.x + second, (self.y + (self.size / 2)) - radii)
            pen.down()
            pen.fillcolor("black")
            pen.begin_fill()
            pen.circle(radii)
            pen.end_fill()
            pen.up()


if __name__ == '__main__':
    a = Die(0, -100, 300)
    a.draw()
