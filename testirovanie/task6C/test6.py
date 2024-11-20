from task6 import Solution
import unittest

class TestCases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_two_roots(self):
        self.assertEqual(self.sol.solve_quadratic(1, -3, 2), "два корня - x1 = 2.0, x2 = 1.0")

    def test_one_root(self):
        self.assertEqual(self.sol.solve_quadratic(1, -2, 1), "один корень - x = 1.0")

    def test_no_real_roots(self):
        self.assertEqual(self.sol.solve_quadratic(1, 2, 5), "нет действительных корней.")

    def test_zero_a(self):
        self.assertEqual(self.sol.solve_quadratic(0, 2, 3), "ошибка")

    def test_fractional_coefficients(self):
        self.assertEqual(self.sol.solve_quadratic(0.5, -2, 0.5), "два корня - x1 = 2.0, x2 = -2.0")

    def test_all_zero_coefficients(self):
        self.assertEqual(self.sol.solve_quadratic(0, 0, 0), "ошибка")

if __name__ == '__main__':
    unittest.main()
