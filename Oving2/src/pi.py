import math


def ArchimedesPI(n):
    s = 1
    for x in range(30):
        s2 = s / 2
        a = math.sqrt(1 - math.pow(s2, 2))
        b = 1 - a
        p = n * s
        s = math.sqrt(pow(b, 2) + pow(s2, 2))
        pi = p / 2
        n = n * 2
    return pi


if __name__ == '__main__':
    a = ArchimedesPI(6)
    b = math.pi
    print(a)
    print('Difference:', a - b)
