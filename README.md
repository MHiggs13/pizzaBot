# Michael Higgins PizzaBot for Slice

Pizzabot delivers pizzas in a neighborhood. Given a grid of houses (each point on the grid is a house) and a list of houses within the grid to deliver to, pizza bot will travel to each house that requires a delivery and "deliver" a pizza.
Pizzabot can be given one of the following instructions,
N: Move north
S: Move south
E: Move east
W: Move west
D: Drop pizza

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need Python 3 to run pizzaBot. 
On Ubuntu Python 3 can be installed by calling:

```$ sudo apt-get install python3 python3-pip```

### Running
To run pizza bot, call python3 with the arguments pizzaBot.py and the parameters that are passed into the pizzabot.

```python3 ./pizzaBot.py "5x5 (0, 0) (1, 3) (2, 2)" ```

The parameters passed in should follow this exact format.
```
5x5 - (NxN) - is the width and height of the grid
(0, 0) - (N, N) - is a list of all houses, to deliver pizzas to
```
Once completed the pizzaBot will output the instructions it carried out to deliver to all houses on it's delivery list.

```
python3 ./pizzaBot.py "5x5 (0, 0) (1, 3) (2, 2)"
DNNNNNESSDSSSENND
```

## Running the tests

To run the tests, navigate to the source code directory and run
```python3 -m unittest```

Errors and failures will be displayed on the command line.

Tests focus on the pizzaBot.py and driver.py files, to test the functionality of the methods which control the flow of the program and the Driver class.
