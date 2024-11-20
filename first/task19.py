import cmath

class Task19:

    def urav(self, a: float, b: float, c: float):
        d = b**2 - 4*a*c
        kor = (-b + cmath.sqrt(d)) / (2 * a)
        kor1 = (-b - cmath.sqrt(d)) / (2 * a)
        return kor, kor1

a = float(input(""))
b = float(input(""))
c = float(input(""))
task19 = Task19()

res = task19.urav(a, b, c)
print(res)