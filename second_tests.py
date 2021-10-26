import pytest
from app.calculator import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 4, 3) == 12

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_adding_calculate_corrently(self):
        assert self.calc.adding(self, 5, 3) == 8

    def test_subtraction_calculate_corrently(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def teardown(self):
        self.calc.dispose()


