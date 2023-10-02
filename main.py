def is_password_good(password):
    try:
        # Проверка длины пароля
        if len(password) < 8:
            raise ValueError("Пароль слишком короткий (менее 8 символов)")

        # Проверка наличия хотя бы одной заглавной буквы
        if not any(c.isupper() for c in password):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")

        # Проверка наличия хотя бы одной цифры
        if not any(c.isdigit() for c in password):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")

        # Если все проверки пройдены, возвращаем True
        return True

    except ValueError as e:
        print(f"Ошибка: {e}")
        return False

    finally:
        print("Проверка пароля завершена")


while True:
    # Запрос пароля с клавиатуры
    password = input("Введите пароль: ")
    result = is_password_good(password)

    if result:
        print("Пароль надежный")
        break
    else:
        print("Пароль не надежный. Попробуйте еще раз.")
