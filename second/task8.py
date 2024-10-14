class find_st1_in_st:

    def __init__(self, st: str, st1: str):
        self.st = st
        self.st1 = st1

    def check_string(self):
        return self.st.index(self.st1)
    
st = input()
st1 = input()
task8 = find_st1_in_st(st, st1)

result = task8.check_string()
print(result)