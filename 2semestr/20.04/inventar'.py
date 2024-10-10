pred1 = None
pred2 = None
pred3 = None
pred4 = None
pred5 = None
pred6 = None
pred7 = None
vyb = None

def menu():
    print("------------------------------------------------")
    print("Инвентарь")
    print("------------------------------------------------")
    print("1.", pred1)
    print("2.", pred2)
    print("3.", pred3)
    print("4.", pred4)
    print("5.", pred5)
    print("6.", pred6)
    print("7.", pred7)
    print("------------------------------------------------")

    global vyb
    vyb = input()

    if vyb in ["1", "2", "3", "4", "5", "6", "7"]:
        if vyb == "1":
            if pred1 is None:
                vybor2()
            else:
                vybor()
        elif vyb == "2":
            if pred2 is None:
                vybor2()
            else:
                vybor()
        elif vyb == "3":
            if pred3 is None:
                vybor2()
            else:
                vybor()
        elif vyb == "4":
            if pred4 is None:
                vybor2()
            else:
                vybor()
        elif vyb == "5":
            if pred5 is None:
                vybor2()
            else:
                vybor()
        elif vyb == "6":
            if pred6 is None:
                vybor2()
            else:
                vybor()
        elif vyb == "7":
            if pred7 is None:
                vybor2()
            else:
                vybor()
    else:
        print("bb")

def vybor():
    print("1. Заменить")
    print("2. Удалить")

    c = input()

    if c == "1":
        a = input()
        if vyb == "1":
            global pred1
            pred1 = a
        elif vyb == "2":
            global pred2
            pred2 = a
        elif vyb == "3":
            global pred3
            pred3 = a
        elif vyb == "4":
            global pred4
            pred4 = a
        elif vyb == "5":
            global pred5
            pred5 = a
        elif vyb == "6":
            global pred6
            pred6 = a
        elif vyb == "7":
            global pred7
            pred7 = a
        menu()

    elif c == "2":
        if vyb == "1":
            pred1 = None
        elif vyb == "2":
            pred2 = None
        elif vyb == "3":
            pred3 = None
        elif vyb == "4":
            pred4 = None
        elif vyb == "5":
            pred5 = None
        elif vyb == "6":
            pred6 = None
        elif vyb == "7":
            pred7 = None
        menu()

def vybor2():
    print("Что добавить?")
    a = input()
    if vyb == "1":
        global pred1
        pred1 = a
    elif vyb == "2":
        global pred2
        pred2 = a
    elif vyb == "3":
        global pred3
        pred3 = a
    elif vyb == "4":
        global pred4
        pred4 = a
    elif vyb == "5":
        global pred5
        pred5 = a
    elif vyb == "6":
        global pred6
        pred6 = a
    elif vyb == "7":
        global pred7
        pred7 = a
    menu()

menu()