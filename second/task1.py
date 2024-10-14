# здесь создается список последовательности числел и проверяется обычным алгоритмом проверкой на простое число

from math import sqrt

class prostye:

    def is_prime(self, num: int):               # проверка на простое число
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def prime(self, digit: int):
        primes = []
        for num in range(2, digit + 1):         # наполнение списка
            if self.is_prime(num):              # проверка списка
                primes.append(num)
        return primes


task_prime = prostye()
digit = int(input())

prime = task_prime.prime(digit)
print(prime)