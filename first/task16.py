class Task16:

    def check(self, st1: str, st2: str):
        count = 0 

        for char in st1:
            if char in st2:
                count += 1

        return count

st1 = input()
st2 = input()
task16 = Task16()

res = task16.check(st1, st2)
print(res)