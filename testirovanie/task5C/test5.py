from task5 import Solution
import unittest

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_equilateral(self):
        self.assertEqual(self.sol.check_triangle(5, 5, 5), "равносторонний")
    
    def test_isosceles(self):
        self.assertEqual(self.sol.check_triangle(5, 5, 3), "равнобедренный")
    
    def test_right_triangle(self):
        self.assertEqual(self.sol.check_triangle(3, 4, 5), "прямоугольный")
    
    def test_scalene(self):
        self.assertEqual(self.sol.check_triangle(3, 4, 6), "разносторонний")
    
    def test_negative_side(self):
        self.assertEqual(self.sol.check_triangle(-3, 4, 5), "невозможно образовать треугольник")


if __name__ == '__main__':
    unittest.main()
