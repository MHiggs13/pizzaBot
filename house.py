from housingGrid import Point

class House:
    """ A house that has requested a delivery, contains a point and a boolean
    of whether or not the delivery is completed
    """

    def __init__(self,  x, y, isDelivered=False):
        self.p = Point(x, y)
        self.isDelivered = isDelivered

    def __lt__(self, other):
        """ Overriden __lt__ allows a list of houses to be sorted.
        house1 is less than house2, when house1.x is less than house2.x
        when x's are equal,
        and x is even, then house1 is less than house2 when house1.y is less
        than house2.y;
        and x is odd, then house1 is less than house2 when house1.y is more
        than house2.y
        """

        if self.p.x == other.p.x:
            # even x, sort y asc
            if self.p.x % 2 == 0:
                return self.p.y <= other.p.y
            # odd x, sort y desc
            else:
                return self.p.y >= other.p.y
        else:
            return self.p.x < other.p.x

    def __eq__(self, other):
        return self.p == other.p and self.isDelivered == other.isDelivered

    def __str__(self):
        return "Point: {0}\t,isDelivered: {1}".format(str(self.p), self.isDelivered)
