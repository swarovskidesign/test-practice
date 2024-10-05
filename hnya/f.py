class Operacii:

    def main(self):

        print("----------------------------------")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Остаток от деления")
        print("6. Отрицательное число")
        print("7. Возвести в степень")
        print("----------------------------------")

        a = int(input("Выберите операцию - "))

        if a == 1:
            b, c = int(input("Введи первое число ")), int(input("Введи второе число "))
            result = self.pluse(b, c)
            print(result)

        elif a == 2:
            b, c = int(input("Введи первое число ")), int(input("Введи второе число "))
            result = self.minus(b, c)
            print(result)
        
        elif a == 3:
            b, c = int(input("Введи первое число ")), int(input("Введи второе число "))
            result = self.mult(b, c)
            print(result)

        elif a == 4:
            b, c = int(input("Введи первое число ")), int(input("Введи второе число "))
            result = self.div(b, c)
            print(result)

        elif a == 5:
            b, c = int(input("Введи первое число ")), int(input("Введи второе число "))
            result = self.ost(b, c)
            print(result)

        elif a == 6:
            b, c = int(input("Введи первое число ")), int(input("Введи второе число "))
            result = self.otric(b, c)
            print(result)

        elif a == 7:
            b, c = int(input("Введи первое число ")), int(input("Введи второе число "))
            result = self.mult2(b, c)
            print(result)

    def pluse(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b
    
    def ost(self, a, b):
        return a % b
    
    def otric(self, a, b):
        return -a, -b
    
    def mult2(self, a, b):
        return a ** b
    
operacii = Operacii()

operacii.main()