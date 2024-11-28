from task6 import Solution
import unittest

class TestCases(unittest.TestCase):

    def test_two_roots(self):
        self.assertEqual(Solution.solve_quadratic(1, -3, 2), "два корня: x1 = 2.0, x2 = 1.0")

    def test_one_root(self):
        self.assertEqual(Solution.solve_quadratic(1, -2, 1), "один корень: x = 1.0")

    def test_no_real_roots(self):
        self.assertEqual(Solution.solve_quadratic(1, 2, 5), "нет действительных корней.")

    def test_zero_a(self):
        self.assertEqual(Solution.solve_quadratic(0, 2, 3), "линейное уравнение - корень x = -1.5")

    def test_fractional_coefficients(self):
        self.assertEqual(Solution.solve_quadratic(0.5, -2, 0.5), "два корня: x1 = 3.732050807568877, x2 = 0.2679491924311228")

    def test_all_zero_coefficients(self):
        self.assertEqual(Solution.solve_quadratic(0, 0, 0), "решение неопределено")

    def test_non_numeric(self):
        self.assertEqual(Solution.solve_quadratic("a", 2, 3), "ошибка - некорректные коэффициенты")

if __name__ == '__main__':
    unittest.main()
