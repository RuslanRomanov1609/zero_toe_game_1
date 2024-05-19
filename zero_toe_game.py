def look():
    print("Привет!")
    print("Это игра крестики - нолики")
    print("------------")
    print("Для выбора клетки используй координаты X и Y")
    print("Вводи два значения поочередно")
    print("Пример: 1 2, где 1 - X(ширина), 2 - Y(высота) ")
    print('')
def start():
    print()
    print("    | 0 | 1 | 2 |")
    print(" ----------------")
    for i, row in enumerate(square):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ----------------")
    print()
def check():
    while True:
        numbers = input("        Ваш ход:  ").split()

        if len(numbers) != 2:
            print("Введите 2 координаты")
            continue
        x, y = numbers
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Не корректно введены числа')
            continue
        if square[x][y] != " ":
            print("Ячейка занята")
            continue
        return x, y
def winner():
    winner_numb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for numb in winner_numb:
        figures = []
        for c in numb:
            figures.append(square[c[0]][c[1]])
        if figures == ["X", "X", "X"]:
            print("Выиграл игрок Х!!!")
            return True
        if figures == ["0", "0", "0"]:
            print("Выиграл игрок 0!!!")
            return True
    return False

look()
square = [[" "] * 3 for i in range(3)]
counter = 0
while True:
    counter += 1
    start()
    if counter % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")
    x, y = check()
    if counter % 2 == 1:
        square[x][y] = "X"
    else:
        square[x][y] = "0"
    if winner():
        break
    if counter == 9:
        print("Ничья!")
        break
