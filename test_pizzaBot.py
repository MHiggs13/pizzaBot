import unittest
import pizzaBot

class PizzaBotResultChecks(unittest.TestCase):
    def test_simplePath(self):
        self.assertEqual(pizzaBot.main("5x5 (1, 3) (4, 4)"), "NNNNNESSDSSSENNNNNESSSSSENNNND")
