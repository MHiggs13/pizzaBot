import unittest
from driver import Driver
from housingGrid import Grid, Point
from house import House

class TestDriverMove(unittest.TestCase):
    def test_northBoundaryMoveEast(self):
        grid = Grid(5, 5)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 0
        driver.p.y = 5
        driver.goNorth = True

        driver.move()

        expected = Point(1, 5)

        self.assertEqual(driver.p, expected)

    def test_northBoundaryMoveSouth(self):
        grid = Grid(5, 5)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 1
        driver.p.y = 5
        driver.goNorth = False

        driver.move()

        expected = Point(1, 4)

        self.assertEqual(driver.p, expected)


    def test_southBoundaryMoveEast(self):
        grid = Grid(5, 5)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 1
        driver.p.y = 0
        driver.goNorth = False

        driver.move()

        expected = Point(2, 0)

        self.assertEqual(driver.p, expected)

    def test_southBoundaryMoveNorth(self):
        grid = Grid(5, 5)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 2
        driver.p.y = 0
        driver.goNorth = True

        driver.move()

        expected = Point(2, 1)

        self.assertEqual(driver.p, expected)

    def  test_southAndEastBoundary(self):
        grid  = Grid(5, 5)

        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 5
        driver.p.y = 0
        driver.goNorth = False

        driver.move()

        expected = Point(5, 0)

        self.assertEqual(driver.p, expected)


    def  test_northAndEastBoundary(self):
        grid  = Grid(6, 4)

        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 6
        driver.p.y = 4
        driver.goNorth = True

        driver.move()

        expected = Point(6, 4)

        self.assertEqual(driver.p, expected)

class TestDriverMoveDirections(unittest.TestCase):
    def test_moveNorth(self):
        grid = Grid(7, 4)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 0
        driver.p.y = 1
        driver.goNorth = True

        driver.moveNorth()

        expected = Point(0, 2)

        self.assertEqual(driver.p, expected)
        self.assertEqual(driver.actionList[-1], "N")


    def test_moveEast(self):
        grid = Grid(7, 4)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 1
        driver.p.y = 0
        driver.goNorth = False

        driver.moveEast()

        expected = Point(2, 0)

        self.assertEqual(driver.p, expected)
        self.assertEqual(driver.actionList[-1], "E")


    def test_moveSouth(self):
        grid = Grid(7, 4)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 5
        driver.p.y = 3
        driver.goNorth = False

        driver.moveSouth()

        expected = Point(5, 2)

        self.assertEqual(driver.p, expected)
        self.assertEqual(driver.actionList[-1], "S")


    def test_moveWest(self):
        grid = Grid(7, 4)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.p.x = 3
        driver.p.y = 0
        driver.goNorth = False

        driver.moveWest()

        expected = Point(2, 0)

        self.assertEqual(driver.p, expected)
        self.assertEqual(driver.actionList[-1], "W")

class TestDriverSortDeliveries(unittest.TestCase):
    def test_sortDeliveriesNoSwaps(self):
        grid = Grid(7, 4)
        startingHouses = [House(0,1), House(2,3)]
        driver = Driver(grid, startingHouses)

        driver.sortDeliveries()

        expected = [House(0,1), House(2,3)]

        self.assertEqual(driver.deliveryList, expected)

    def test_sortDeliveriesOneSwap(self):
        grid = Grid(7, 4)
        startingHouses = [House(2,3), House(0,1)]
        driver = Driver(grid, startingHouses)

        driver.sortDeliveries()

        expected = [House(0,1), House(2,3)]

        self.assertEqual(driver.deliveryList, expected)

    def test_sortDeliveriesXConflictNorth(self):
        grid = Grid(7, 4)
        startingHouses = [House(0,1), House(0,3)]
        driver = Driver(grid, startingHouses)

        driver.sortDeliveries()

        expected = [House(0,1), House(0,3)]

        self.assertEqual(driver.deliveryList, expected)

    def test_sortDeliveriesXConflictSouth(self):
        grid = Grid(7, 4)
        startingHouses = [House(1,1), House(1,2)]
        driver = Driver(grid, startingHouses)

        driver.sortDeliveries()

        expected = [House(1,2), House(1,1)]

        self.assertEqual(driver.deliveryList, expected)

class TestDriverDelivery(unittest.TestCase):
    def test_driverCompleteDelivery(self):
        grid = Grid(7, 4)
        startingHouses = [House(1,1), House(1,2)]
        driver = Driver(grid, startingHouses)

        driver.completeDelivery(driver.deliveryList[0])

        expected = True

        self.assertEqual(driver.deliveryList[0].isDelivered, expected)
        self.assertEqual(driver.actionList[-1], "D")






