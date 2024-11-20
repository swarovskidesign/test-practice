from math import sqrt

def menu():
    a = int(input())
    if a == 1:
        task1()

    elif a == 2:
        task2()

    elif a == 3:
        task3()

    elif a == 4:
        task4()

def prst(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def task1():
    q = [12, -45, 67, -34, 89, -100, 23, -5, 34]
    for n in q:
        if prst(n):
            print(n, "простое")
        else:
            print(n, "составное")


def task2():
    w = [-90, 56, -23, 12, 45, -67, 89, -32, 11, -76, 54]
    print(sum(w))

def task3():
    e = [3, -15, 27, -48, 59, -6, 14, -38, 72, -94, 18, -12]
    plus, minus = 0, 0
    for num in e:

        if num >=0:
            plus += 1
        else:
            minus += 1

    print(f"{e}\nkolvo plus = {plus}")
    print(f"kolvo minus = {minus}")

def task4():
    r = [-22, 45, -67, 34, -89, 100, -23, 5, -34, 78]
    print(min(r), max(r))

menu()