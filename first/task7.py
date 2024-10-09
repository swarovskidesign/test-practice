from math import sqrt

class Task7:
    def __init__(self):
        self.answer = 'prostoe'
        self.answer1 = 'sostavnoe'

    def taska(self, digit: int):
        self.proverka(digit)
        if self.proverka(digit):
            return self.answer
        else:
            return self.answer1

    def proverka(self, digit: int):
        if digit <= 1:
            return False
        for i in range(2, int(sqrt(digit)) + 1):
            if digit % i == 0:
                return False
        return True


digit = int(input('digit '))
task7 = Task7()

res = task7.taska(digit)
print(res)