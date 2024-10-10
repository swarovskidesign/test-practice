que1 = None
que2 = None
que3 = None
que4 = None
que5 = None

import random

def menu():
    print("------------------------------------------------")
    print("Сгенерированные вопросы")
    print("------------------------------------------------")
    print("1.", pred1)
    print("2.", pred2)
    print("3.", pred3)
    print("4.", pred4)
    print("5.", pred5)
    print("------------------------------------------------")
    a = input()

def main1():
    global que1
    global que2
    global que3
    global que4
    global que5
    print("Какой длины нужен пароль?")
    kolvo = int(input())
    for i in range(5):
        que1 = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%?*/") for i in range(kolvo))
        print("Сгенерированный пароль:", result)

main1()