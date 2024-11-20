class Task3:

    def __init__(self):
        self.hello = 'sup, '

    def hi(self, st: str):
        return self.hello + st
    
st = input('name? ')
task3 = Task3()  

res = task3.hi(st)
print(res)