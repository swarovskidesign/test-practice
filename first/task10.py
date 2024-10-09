class Task10:

    def zapolnenie(self, lst: list):
        while True:
            try:
                digit = int(input('ur digit (for cancel (q)) ' ))
                lst.append(digit)
            except ValueError:
                break

        return lst

    def summator(self, lst: list):
        self.zapolnenie(lst)
        return sum(lst)
    
    def arif(self, lst: list):
        return self.summator(lst) // len(lst)


lst = []
task10 = Task10()

res = task10.arif(lst)
print(res)