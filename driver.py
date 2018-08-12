from housingGrid import Point

class Driver:
    """ Delivers pizzas to locations that are marked on a Grid.
    Drivers travel north when on an even x point, and south when on an odd
    x point. When the y equals the width or 0 then the Driver moves East and
    continues it's process until all pizzas have been delivered.

    Pizza is delivered when a driver is on the same point as a house that has
    requested a delivery.

    The list of deliveries is SORTED so that houses with the same x point can
    be completed close together. See House class for information on sorting,
    the sorting is crucial to how the Driver navigates and the Driver's success.
    """

    def __init__(self, grid, startingHouses, x=0, y=0):
        """ Driver will goNorth by default and only does not goNorth
        if the driver's starting position is at the top of the grid 
        instead of the bottom.

        grid: the square grid to deliver pizzas on
        startingHouses: the list of houses to deliver to
        x: initial x point of driver
        y: initial y point of driver
        """
        self.grid = grid
        self.deliveryList = startingHouses
        self.p = Point(x, y)
        self.actionList = ""

        # if we are at bottom of the grid we start by going North (increasing y)
        if self.p.y == 0:
            self.goNorth = True
        elif self.p.y == self.grid.height:
            self.goNorth = False
        else:
            # default to go north
            self.goNorth = True

    def deliver(self):
        """ Deliver to each house in deliveryList.
        Systematically move through the grid, going north when
        x is even and then when the max y is reached, moving east
        and going south  until 0 is reached. This continues until all 
        deliveries are completed or the driver moves beyond the width or
        height of the grid """
        self.sortDeliveries()

        # sorted by x coords then y
        # so go to each x and deliver at any y's in that colummn
        for house in self.deliveryList:
            while not house.isDelivered and self.p.x <= self.grid.width and (
                self.p.y <= self.grid.height):
                if (self.p == house.p):
                    self.completeDelivery(house)
                else:
                    self.move()

    def completeDelivery(self, house):
        house.isDelivered = True
        self.actionList += "D"

    def move(self):
        if self.p.y == self.grid.height:
            if self.goNorth:
                self.goNorth = False
                self.moveEast()
            else:
                self.moveSouth()
        elif self.p.y == 0:
            if not self.goNorth:
                self.goNorth = True
                self.moveEast()
            else:
                self.moveNorth()
        else:
            if self.goNorth:
                self.moveNorth()
            else:
                self.moveSouth()

    def moveNorth(self):
        self.p.y += 1
        self.actionList += "N"

    def moveEast(self):
        self.p.x += 1
        self.actionList += "E"

    def moveSouth(self):
        self.p.y -= 1
        self.actionList += "S"

    def moveWest(self):
        self.p.x -= 1
        self.actionList += "W"

    def sortDeliveries(self):
        self.deliveryList = sorted(self.deliveryList)

    def __str__(self):
        return "Driver at : {0}".format(self.p)
