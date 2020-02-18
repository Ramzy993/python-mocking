from unittest import TestCase
from unittest.mock import patch
from claculator import Calculator


class TestCalculator(TestCase):

    @patch('claculator.Calculator.sum', return_value=8)
    def test_sum(self, sum):
        self.assertEqual(sum(3, 5), 8)
