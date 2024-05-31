
import unittest
from Ripasso.ripasso import calc # questo metodo di import si chiama import relativo 
# import relativo sintassi = "from..nome_directori.nome_file import nome funzione o classe  "

class TestCalculations(unittest.TestCase):

    def setup(self):

        self.calculations = calc(8,2)

    def test_sum(self):

        self.assertEqual(self.calculations.get_sum(), 10, "the sum is wrong")

    def test_sum(self):

        self.assertEqual(self.calculations.get_sum(), 7, "the sum is wrong")

if __name__== "__main__":
    unittest.main()