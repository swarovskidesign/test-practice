# тут я взял задачу из прошлого уровня и дописал в 11 строке только <[-1]>

class Task2:

    def __init__(self):
        self.digit1 = self.digit2 = 1

    def run(self, digit: int):
        lst = []
        self.fib(digit, lst)
        return lst[-1]

    def fib(self, digit: int, lst: list):
        for _ in range(digit):
            lst.append(self.digit1)
            self.digit1, self.digit2 = self.digit2, self.digit1 + self.digit2

digit = int(input('digit '))
task2 = Task2()

res = task2.run(digit)
print(res)