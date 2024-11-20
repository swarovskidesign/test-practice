import asyncio

class Solver:
    def __init__(self, equa, lst):
        self.equa = equa
        self.lst = lst
        self.step1 = []
        self.step2 = []

    async def zapolnenie(self, a):
        while a < 2:
            digit = int(input(f"значение {a+1}: "))
            self.lst.append(digit)
            a += 1
        return self.lst

    async def x(self, e):
        for diapazon in range(self.lst[0], self.lst[1] + 1, e):
            self.step1.append(diapazon)
            await asyncio.sleep(0)
        return self.step1

    async def y(self):
        for yy in self.step1:
            result = eval(self.equa.replace('x', str(yy)))
            self.step2.append(result)
            await asyncio.sleep(0)
        return self.step2

    def get_intersection_points(self):
        a, b = None, None
        for i in range(len(self.step1) - 1):
            if self.step2[i] * self.step2[i + 1] < 0:
                a = self.step1[i]
                b = self.step1[i + 1]
                break
        return a, b
