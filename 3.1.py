while True:
    try:
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))
        if n <= 0 or m <= 0:
            raise ValueError
        break
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")

# Создаем двумерный массив и заполняем его символами в шахматном порядке
arr = []
for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:
            row.append("%")
        else:
            row.append("&")
    arr.append(row)


# Ставим точку в левый верхний угол
arr[0][0] = "."

# Выводим массив на экран
for row in arr:
    print(" ".join(row))
