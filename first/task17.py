class Task17:

    def bukva(self, st: str):
        dict = {}
        for char in st:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        return dict

st = input("")
task17 = Task17()


res = task17.bukva(st)
print(res)