class Calculator:

    def complete_exercise(exercise: str) -> float:          #  здесь конструкция (->) нужна, потому что подается string, а вывод нужен float
        try:
            result = eval(exercise)                         # eval конвертирует строку в математическое(python) - выражение и вычисляет его
        except (SyntaxError, ZeroDivisionError):
            return 'некорректный ввод'
        return result


calc = Calculator()
exercise = input()


result = calc.complete_exercise(exercise)
print(result)
