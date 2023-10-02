def divide(x, y):
    try:
        result = x / y
        print("Результат деления:", result)
    except ZeroDivisionError:
        print("Деление на ноль невозможно")


try:
    x = float(input("Введите делимое : "))

    y = float(input("Введите делитель: "))

    divide(x, y)
except ValueError:
    print("Ошибка: Введите корректное числовое значение")
