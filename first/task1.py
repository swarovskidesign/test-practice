class Task1:

    def run(self, a: float, b: float) -> float:
        return a + b

task1 = Task1()

a = float(input('first digit: '))
b = float(input('second digit: '))

res = task1.run(a, b)
print(res)