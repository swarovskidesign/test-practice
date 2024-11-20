import random
import string

def menu():
    print("----------------------------------------------")
    print("Какой пароль тебе нужен?")
    print("----------------------------------------------")
    print("1. С цифрами")
    print("2. С цифрами и заглавными буквами")
    print("3. С цифрами, заглавными буквами и символами")
    print("----------------------------------------------")

    a = input()

    if a == "1":
            main1()
    elif a == "2":
            main2()
    elif a == "3":
            main3()

def main1():
    global kolvo
    print("Какой длины нужен пароль?")
    kolvo = int(input())
    b = string.digits + string.ascii_lowercase
    for i in range(5):
        result = ''.join(random.choice(b) for i in range(kolvo))
        print("Сгенерированный пароль:", result)

def main2():
    global kolvo
    print("Какой длины нужен пароль?")
    kolvo = int(input())
    for i in range(5):
        result = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(kolvo))
        print("Сгенерированный пароль:", result)

def main3():
    global kolvo
    print("Какой длины нужен пароль?")
    kolvo = int(input())
    for i in range(5):
        result = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%?*/") for i in range(kolvo))
        print("Сгенерированный пароль:", result)
menu()