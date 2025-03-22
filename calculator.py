def calculate(expression: str) -> str:
    expression = expression.strip()

    if '+' in expression:
        operator = '+'
    elif '-' in expression:
        operator = '-'
    elif '*' in expression:
        operator = '*'
    elif '/' in expression:
        operator = '/'
    elif '^' in expression:
        operator = '^'
    else:
        raise ValueError("Строка не является математической операцией")

    parts = expression.split(operator)

    if len(parts) != 2:
        raise ValueError("Неверный формат ввода. Ожидается два операнда и один оператор.")

    try:
        a = float(parts[0].strip())
        b = float(parts[1].strip())
    except ValueError:
        raise ValueError("Операнды должны быть числами.")

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("Ошибка: Деление на ноль.")
        result = a / b
    elif operator == '^':
        result = a ** b

    return str(result)


if __name__ == "__main__":
    while True:
        try:
            input_expression = input("Введите арифметическое выражение (или 'exit' для выхода): ")
            if input_expression.lower() == 'exit':
                print("Выход из программы.")
                break

            output = calculate(input_expression)
            print(f"Результат: {output}")
        except Exception as e:
            print(f"Ошибка: {e}")
