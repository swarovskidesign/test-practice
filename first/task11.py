class Task11:

    def run(self, lst: list):
        return max(lst)
    
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
task11 = Task11()

res = task11.run()
print(res)