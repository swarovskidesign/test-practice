import math

class Solution:

    @staticmethod
    def check_triangle(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return "ошибка - Стороны должны быть положительными"
        
        if a + b <= c or a + c <= b or b + c <= a:
            return "ошибка - Стороны не могут образовать треугольник"
        
        if a == b == c:
            return "равносторонний"
        
        if math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2):
            if a == b or b == c or a == c:
                return "равнобедренный прямоугольный"
            return "прямоугольный"
        
        if a == b or b == c or a == c:
            return "равнобедренный"
        return "разносторонний"
