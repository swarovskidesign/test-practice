from task5 import Solution
import unittest

class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(Solution.check_triangle(5, 5, 5), "равносторонний")
    
    def test_isosceles(self):
        self.assertEqual(Solution.check_triangle(5, 5, 3), "равнобедренный")
    
    def test_right_triangle(self):
        self.assertEqual(Solution.check_triangle(3, 4, 5), "прямоугольный")
    
    def test_scalene(self):
        self.assertEqual(Solution.check_triangle(3, 4, 6), "разносторонний")
    
    def test_negative_side(self):
        self.assertEqual(Solution.check_triangle(-3, 4, 5), "ошибка - Стороны должны быть положительными")
    
    def test_zero_side(self):
        self.assertEqual(Solution.check_triangle(0, 4, 5), "ошибка - Стороны должны быть положительными")
    
    def test_invalid_triangle(self):
        self.assertEqual(Solution.check_triangle(1, 2, 3), "ошибка - Стороны не могут образовать треугольник")


if __name__ == '__main__':
    unittest.main()
