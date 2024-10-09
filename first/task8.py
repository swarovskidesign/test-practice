class Task8:
    
    def run(self, st: str):
        self.reversed_str = ""
        
        for i in range(len(st) - 1, -1, -1):
            self.reversed_str += st[i]
        
        return self.reversed_str

st = input('ur txt ')
task8 = Task8()

res = task8.run(st)
print(res)