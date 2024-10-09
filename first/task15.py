class Task15:

    def razdelenie(self, digit: int, lst: list):

        while digit > 0:
            lst.append(digit % 10)
            digit //= 10
        return lst
    
    def itog(self, lst: list):
        lst = []
        self.razdelenie(digit, lst)
        return (sum(lst))
    
lst = []
digit = 1234
task15 = Task15()

res = task15.itog(digit)
print(res)