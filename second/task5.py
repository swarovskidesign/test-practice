class Task10:

    def __init__(self, lst):
        self.lst = lst

    def zapolnenie(self):
        while True:
            word = input('Введите слово (или "q" для завершения): ')
            if word.lower() == 'q':
                break
            self.lst.append(word)

    def find_anagrams(self):
        for word in self.lst:
        