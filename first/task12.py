class Task12:

    def __init__(self):
        self.digit1 = self.digit2 = 1

    def run(self, digit: int):
        lst = []
        self.fib(digit, lst)
        return lst

    def fib(self, digit: int, lst: list):
        for _ in range(digit):
            lst.append(self.digit1)
            self.digit1, self.digit2 = self.digit2, self.digit1 + self.digit2

digit = int(input('digit '))
task12 = Task12()

res = task12.run(digit)
print(res)