

class Grid:
    """ A square grid of width * height dimensions """

    def __init__(self, w = 5, h = 5):
        """ Grid can be initialized with passed in width and height,
        defaults to a width of 5 and a height of 5
        """
        self.width = w
        self.height = h

class Point:
    """ A point in a grid, an x and a y """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

