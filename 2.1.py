import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def process_input(input_data):
    try:
        if isinstance(input_data, list):
            # Найти среднее геометрическое чисел в списке
            product = 1
            for num in input_data:
                product *= num
            geometric_mean = math.pow(product, 1 / len(input_data))
            return f"Среднее геометрическое: {geometric_mean}"

        elif isinstance(input_data, dict):
            # Отсортировать словарь по значению в порядке убывания
            sorted_dict = dict(sorted(input_data.items(), key=lambda item: item[1], reverse=True))
            for key, value in sorted_dict.items():
                if is_prime(value):
                    sorted_dict[key] = f"{value} - простое число"
                else:
                    sorted_dict[key] = f"{value} - не простое число"
            return sorted_dict

        elif isinstance(input_data, str):
            # Найти количество слов в строке и вывести самое длинное слово
            words = input_data.split()
            longest_word = max(words, key=len)
            return f"Количество слов: {len(words)}, Самое длинное слово: {longest_word}"

        elif isinstance(input_data, int):
            # Если передано число, определить, является ли оно простым или нет
            if is_prime(input_data):
                return f"{input_data} - простое число"
            else:
                return f"{input_data} - не простое число"

        else:
            return "Недопустимый ввод"

    except Exception as e:
        return f"Ошибка: {e}"


def menu():
    while True:
        # Список
        data_list = [-5, -5, -1, -2, 4, 4, 1, 1, 1]

        # Словарь
        data_dict = {'a': 111, 'b': 122, 'c': 566, 'd': 405, 'e': 21, 'f': 266}

        # Число
        data_number = 17

        # Строка
        data_string = "Привет , это я , моё имя - Марина"

        try:

            while True:

                print("\nМеню:"
                      "\n1. Список"
                      "\n2. Словарь"
                      "\n3. Число целое"
                      "\n4. Строка"
                      "\nДругое. Выход")

                choice = input("\nВыбирете тип, который вы хотите передать функции: ")

                if choice == "1":
                    print("\nРезультат выполнения задачи со списками:", data_list)
                    print("\n", process_input(data_list))

                elif choice == "2":
                    print("\nРезультат выполнения задачи со словарём:", data_dict)
                    print("\n", process_input(data_dict))

                elif choice == "3":
                    print("\nРезультат выполнения задачи с целым числом:", data_number)
                    print(process_input(data_number))

                elif choice == "4":
                    print("\nРезультат выполнения задачи со строками:", data_string)
                    print("\n", process_input(data_string))

                else:
                    return

        except Exception as e:
            f"Ошибка: {e}"


menu()
