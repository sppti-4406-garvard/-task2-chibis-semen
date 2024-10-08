import numpy as np
print("Добрый день! Эта программа для задания 2 (с использованием numpy).")
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Введите значение для элемента [{i+1}, {j+1}]: "))
        row.append(value)
    matrix.append(row)

# Вывод матрицы
print("Созданная матрица:")
for row in matrix:
    print(row)
print('Нажмите 1 чтобы продолжить, или любую другую кнопку чтобы завершить программу.')

cont = int(input())
if cont == 1:
    print('-Введите 1 чтобы транспонировать матрицу')
    print('-Введите 2 чтобы умножить Вашу матрицу на другую')
    print('-Введите 3 чтобы найти ранг матрицы')

    choose = int(input())

    if choose == 1:
        transposed = np.transpose(matrix)
        print('Транспонированная матрица:')
        for row in transposed: print(row)
    elif choose == 2:
        rows2 = int(input("Введите количество строк: "))
        cols2 = int(input("Введите количество столбцов: "))

        matrix2 = []

        for i in range(rows2):
            row = []
            for j in range(cols2):
                value2 = int(input(f"Введите значение для элемента [{i + 1}, {j + 1}]: "))
                row.append(value2)
            matrix2.append(row)
        print("Созданная матрица:")
        for row in matrix2:
            print(row)
        print('Результат умножения:')
        print(np.dot(matrix,matrix2))

    elif choose == 3:
        rank = np.array(matrix)
        print('Ранг Вашей матрицы:',np.linalg.matrix_rank(rank))


else:
    exit()