""" Circuritous, LLC -
An Advanced Circle Analytics Company """

import math


class Circle(object):  # New-style class
    """An advanced circle analytic toolkit"""

    # Flyweight design pattern suppresses the instance dictionary
    __slots__ = ['diameter']
    version = '0.6'  # class variable. Use strings for version code

    # Not an constructor. It is an initializer that takes the existing instance self and populates it
    # takes radius and stores it in dictionary
    def __init__(self, radius):
        self.radius = radius  # instance variable

    #   Gets radius from stored diameter
    @property
    def radius(self):  # Convert dotted access to method calls
        """Radius of circle"""
        return self.diameter / 2.0

    # Sets diameter since it can't be stored
    #  input: radius
    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    #  static so it does not get called by people who don't need it
    #  input: A given angle (example a slope)
    #  Output: Percentage grade of angle
    @staticmethod  # attach functions to classes
    def angle_to_angle(angle):
        """Convert angle in degree to a percentage grade"""
        return math.tan(math.radians(angle)) * 100.0

    # Regular methods has self as an argument
    # Everything that runs inside a method is basically an own module
    # Output: Area inside a circle
    def area(self):
        """Preform quadrature on shape of uniform radius"""
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    #   Output: Perimeter of circle
    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter  # __ makes sure self only references you and not subclasses

    # Make alternative constructors for different uses of the class
    @classmethod
    def from_bbd(cls, bbd):  # Alternative constructor
        """Construct a circle from a bounding box diagonal"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)


# subclass of circle
class Tire(Circle):
    """"Tiers are circles with a corrected perimeter"""

    # Extends the parent method since the parent is called
    # Overriding when parent is not called
    # output: A perimeter of a circle when a layer of material is added to the outside
    def perimeter(self):
        """"Circumference corrected for the rubber"""
        return Circle.perimeter(self) * 1.25

    __perimeter = perimeter


if __name__ == "__main__":
    print('Circuituous version', Circle.version)
    c = Circle(10)
    print('A circle of radius', c.radius)
    print('Has an area of', c.area())
