class Task4:

    def run(self, gradusy: int) -> int:
        f = (gradusy * (9 / 5)) + 32
        return f
    
gradusy = int(input('digit '))
task4 = Task4()

res = task4.run(gradusy)
print(res)