class Task5:

    def run(self, digit: int):
        return digit * digit
    
digit = int(input('digit '))
task5 = Task5()

res = task5.run(digit)
print(res)