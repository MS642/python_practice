class Line:
    """
    Problem 1 Fill in the Line
        class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

        # EXAMPLE OUTPUT
        coordinate1 = (3, 2)
        coordinate2 = (8, 10)

        li = Line(coordinate1, coordinate2)
        li.distance()
            9.433981132056603
        li.slope()
            1.6
    """

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def distance(self):
        x1, y1 = self.point_1
        x2, y2 = self.point_2
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    def slope(self):
        x1, y1 = self.point_1
        x2, y2 = self.point_2
        return (y2 - y1) / (x2 - x1)


coord_1 = (3, 2)
coord_2 = (8, 10)
li = Line(coord_1, coord_2)
assert li.distance() == 9.433981132056603
assert li.slope() == 1.6


class Cylinder:
    """
    Problem 2
        # EXAMPLE OUTPUT
        c = Cylinder(2,3)
        c.volume()
            56.52
        c.surface_area()
            94.2
    """
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.height * self.radius**2

    def surface_area(self):
        return 2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius**2


c = Cylinder(2, 3)
assert c.volume() == 56.52
assert c.surface_area() == 94.2
