import cmath

class Solution:

    def solve_quadratic(a, b, c):
        if a == 0:
            raise ValueError("a != 0")
        
        D = b**2 - 4 * a * c
        
        if D > 0:
            x1 = (-b + cmath.sqrt(D)) / (2 * a)
            x2 = (-b - cmath.sqrt(D)) / (2 * a)
            return (x1, x2)
        elif D == 0:
            x = -b / (2 * a)
            return (x)
        else:
            x1 = (-b + cmath.sqrt(D)) / (2 * a)
            x2 = (-b - cmath.sqrt(D)) / (2 * a)
            return (x1, x2)
