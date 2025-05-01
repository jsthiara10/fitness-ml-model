# tests/test_calculations.py

import unittest
from calorie_predictor import calculate_bmr, calculate_tdee


class TestCalorieFunctions(unittest.TestCase):

    def test_bmr_male(self):
        result = calculate_bmr(weight=70, height=175, age=25, gender='M')
        expected = 10 * 70 + 6.25 * 175 - 5 * 25 + 5
        self.assertAlmostEqual(result, expected)

    def test_bmr_female(self):
        result = calculate_bmr(weight=60, height=165, age=30, gender='F')
        expected = 10 * 60 + 6.25 * 165 - 5 * 30 - 161
        self.assertAlmostEqual(result, expected)

    def test_tdee_moderate(self):
        bmr = 1600
        result = calculate_tdee(bmr, 'moderate')
        expected = 1600 * 1.55
        self.assertAlmostEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
