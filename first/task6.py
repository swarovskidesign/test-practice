class Task6:

    def __init__(self):
        self.binar = 1

    def fact(self, digit: int):

        for i in range(1, digit + 1):
            self.binar *= i

        return self.binar

digit = int(input('digit '))    
task6 = Task6()

res = task6.fact(digit)
print(res)