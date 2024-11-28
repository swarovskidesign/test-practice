from task1_1_1 import Solution
import unittest

class TestSolveQuadratic(unittest.TestCase):

    def test_two_real_roots(self):
        result = Solution.solve_quadratic(1, -3, 2)
        self.assertCountEqual(result, (2.0, 1.0))  # Проверка без учёта порядка

    def test_one_real_root(self):
        result = Solution.solve_quadratic(1, -2, 1)
        self.assertEqual(result, (1.0,))

    def test_two_complex_roots(self):
        result = Solution.solve_quadratic(1, 2, 5)
        self.assertCountEqual(result, ((-1+2j), (-1-2j)))

    def test_not_quadratic(self):
        with self.assertRaises(ValueError):
            Solution.solve_quadratic(0, 2, 5)

    def test_large_coefficients(self):
        result = Solution.solve_quadratic(1e6, -3e6, 2e6)
        self.assertAlmostEqual(result[0], 2.0, places=6)
        self.assertAlmostEqual(result[1], 1.0, places=6)

    def test_small_coefficients(self):
        result = Solution.solve_quadratic(1e-6, -3e-6, 2e-6)
        self.assertAlmostEqual(result[0], 2.0, places=6)
        self.assertAlmostEqual(result[1], 1.0, places=6)

if __name__ == "__main__":
    unittest.main()
