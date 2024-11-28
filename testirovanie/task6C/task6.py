import math

class Solution:

    @staticmethod
    def solve_quadratic(a, b, c):
        if not all(isinstance(i, (int, float)) for i in [a, b, c]):
            return "ошибка - некорректные коэффициенты"
        
        if a == 0:
            if b == 0:
                return "ошибка - не является уравнением" if c != 0 else "решение неопределено"
            x = -c / b
            return f"линейное уравнение - корень x = {x}"
        
        D = b**2 - 4 * a * c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return f"два корня: x1 = {x1}, x2 = {x2}"
        elif D == 0:
            x = -b / (2 * a)
            return f"один корень: x = {x}"
        else:
            return "нет действительных корней."
