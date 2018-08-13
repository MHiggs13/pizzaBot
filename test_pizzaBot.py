import unittest
from pizzaBot import *

class PizzaBotResultChecks(unittest.TestCase):
    def test_simplePath(self):
        self.assertEqual(main("5x5 (1, 3) (4, 4)"), "NNNNNESSDSSSENNNNNESSSSSENNNND")

    def test_inputOddError(self):
        expected = oddError
        self.assertEqual(main("5x5 (1, 3) (4, )"), expected)

    def test_inputLengthError(self):
        expected = lengthError
        self.assertEqual(main("5x5"), expected)
