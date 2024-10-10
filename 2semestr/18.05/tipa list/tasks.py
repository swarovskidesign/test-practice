sentences = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]

while True:
    print("----------------------")
    print("Список задач")
    print("----------------------")
    for i, sentence in enumerate(sentences):
        print(f"{i+1}. {sentence}")

    print("\nМеню:")
    print("===================================")
    print("1. добавить задачу")
    print("2. изменить задачу")
    print("3. удалить задачу")
    print("4. пока")
    print("===================================")

    a = input("что нужно")

    if a == "1":
        new_sentence = input("введи новое")
        sentences.append(new_sentence)
    elif a == "2":
        index = int(input("введни номер задачи")) - 1
        new_sentence = input("введи новое")
        sentences[index] = new_sentence
    elif a == "3":
        index = int(input("введни номер задачи")) - 1
        del sentences[index]
    elif a == "4":
        print("bb")
        break
    else:
        print("неверно")
