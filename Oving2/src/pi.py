import math


def pi(sides, radii, turns):
    diameter = radii * 2
    length = radii
    for x in range(turns):
        if x != 0:
            sides = sides * 2
        halfLength = length / 2
        a = math.sqrt(1 - halfLength ** 2)
        b = 1 - a
        p = sides * length
        length = math.sqrt(b ** 2 + halfLength ** 2)
        approximation = p / diameter
        print(approximation)


pi(6, 1, 14)
