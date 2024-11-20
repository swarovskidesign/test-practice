import math

class Solution:

    def solve_quadratic(a, b, c):
        if a == 0:
            return "ошибка"
        
        D = b**2 - 4 * a * c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return f"два корня: x1 = {x1}, x2 = {x2}"
        elif D == 0:
            x = -b / (2 * a)
            return f"один корень - x = {x}"
        else:
            return "нет действительных корней."
