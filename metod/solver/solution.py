class metod:
    def __init__(self, func, tolerance=1e-5):
        self.func = func
        self.tolerance = tolerance

    def find_root(self, a, b):
        if self.func(a) * self.func(b) >= 0:
            raise ValueError("Функция должна иметь разные знаки в точках a и b.")

        while abs(b - a) >= self.tolerance:
            c = b - (self.func(b) * (b - a)) / (self.func(b) - self.func(a))
            if abs(self.func(c)) < self.tolerance:
                return c
            a, b = b, c
        return c
