import random

questions = [
    "Какое твоё любимое время года?",
    "Кем ты мечтал стать в детстве?",
    "Как дела?",
    "Какое твоё любимое блюдо?",
    "Какой твой любимый фильм?",
    "Какой город ты хотел бы посетить?",
    "Каким видом спорта ты занимаешься?",
    "Какую музыку ты слушаешь?"
]

answers = [
    "Лето",
    "В детстве я мечтал стать гиганским космическим крабом",
    "Нормально",
    "Мое любимое блюдо – пицца",
    "'Интерстеллар'",
    "Я хотел бы посетить Париж",
    "Я занимаюсь бегом",
    "Я слушаю попсу"
]

def add_question():
    question = input("Введите новый вопрос: ")
    questions.append(question)
    print("Вопрос добавлен.")

def add_answer():
    answer = input("Введите новый ответ: ")
    answers.append(answer)
    print("Ответ добавлен.")

def generate_que():
    question = random.choice(questions)
    answer = random.choice(answers)
    return question, answer

def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить вопрос")
        print("2. Добавить ответ")
        print("3. Сгенерировать случайный вопрос и ответ")
        print("4. Выйти")
        vybor = input("Выберите пункт меню (1-4): ")

        if vybor == "1":
            add_question()
        elif vybor == "2":
            add_answer()
        elif vybor == "3":
            q, a = generate_que()
            print(f"\nВопрос: {q}\nОтвет: {a}\n")
        elif vybor == "4":
            print("Выход из программы.")
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите пункт меню от 1 до 4.")


menu()
