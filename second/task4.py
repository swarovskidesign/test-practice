# также взял код с прошлого уровня и добавил параметр строки <lower()>

class Task9:
    
    def __init__(self):
        self.original = st
        self.reversed_str = ""
        self.answer1 = 'polindrom'
        self.answer2 = 'no polidrom'

    def revers(self, st: str):
        for i in range(len(st) - 1, -1, -1):
            self.reversed_str += st[i]

        return self.reversed_str
        
    
    def last(self, st: str):
        self.revers(st)
        if self.revers(st).lower() == self.original.lower():  # added <lower()>
            return self.answer1
        else:
            return self.answer2


st = input('ur txt ')
task9 = Task9()

res = task9.last(st)
print(res)