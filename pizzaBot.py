import sys
import re
from housingGrid import Grid
from driver import Driver
from house import House

lengthError = "error: not enough points passed in for grid and or houses, should be at least 4 digits"
oddError = "error: odd number of total x and y values for grid and or houses, should be even"

def initializePizzaBot(gridSize, houses):
    """
    Creates grid and creates driver, returns driver

    gridSize: list of size 2 with the width and height of a grid
    houses: list of house x and y points, first element is an x and it's 
    associated y follows
    """
    grid = Grid(gridSize[0],  gridSize[1])

    startingHouses = []
    for count in range(int(len(houses)/2)):
        startingHouses.append(House(houses[count*2], houses[count*2+1]))

    driver = Driver(grid, startingHouses)

    return driver

def main(args):
    args = [int(s) for s in re.split('x| \(|, |\)', args) if s.isdigit()]

    if len(args) >= 4 and len(args) % 2 == 0:
        gridSize = [args[0], args[1]]
        houses = args[2:]

        driver = initializePizzaBot(gridSize, houses)

        driver.deliver()
        return(driver.actionList)
    else:
        if len(args) < 4:
            return lengthError
        elif len(args) % 2 != 0:
            return oddError

if __name__ == "__main__":

    print(main(sys.argv[1]))
