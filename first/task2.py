class Task2:

    def __init__(self, a: int):
        self.chet = 'Chetnoe'
        self.nochet = 'Ne chetnoe'


    def sverka1(self, a: int):
        if a % 2 == 0:
            return self.chet
        else:
            return self.nochet


a = float(input('digit '))
task2 = Task2(a)

res = task2.sverka1(a)
print(res)