def multiply(matrix, number):               #функция умножения матрицы 3x3 на число

    result_matrix = [
        [matrix[0][0] * number, matrix[0][1] * number, matrix[0][2] * number],
        [matrix[1][0] * number, matrix[1][1] * number, matrix[1][2] * number],
        [matrix[2][0] * number, matrix[2][1] * number, matrix[2][2] * number]
    ]

    return result_matrix


def minor(matrix):                 #функция нахождения матрицы миноров (3x3)
    minor_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Вычисляем миноры
    minor_matrix[0][0] = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
    minor_matrix[0][1] = matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]
    minor_matrix[0][2] = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]

    minor_matrix[1][0] = matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]
    minor_matrix[1][1] = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]
    minor_matrix[1][2] = matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]

    minor_matrix[2][0] = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
    minor_matrix[2][1] = matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]
    minor_matrix[2][2] = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return minor_matrix



def transpose (rows,cols,matrix):                     #функция транспонирования
    transposed = [[0 for i in range(rows)] for i in range(cols)]
    for i in range (rows):
        for j in range(cols):
            transposed[j][i]=matrix[i][j]
    return transposed



def multiplication(a,b):                                               #функция умножения матриц
    if len(a[0]) != len(b):
        raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице")
    res = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    # Умножаем матрицы
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]

    print("Результат умножения:")
    for row in res:
        print(row)


def determinant(a):     #функция для нахождения определителя матрицы
    if len(a) == 2:
        det = (a[0][0]*a[1][1])-(a[0][1]*a[1][0])
        return det
    elif len(a) == 3:
        det = a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1]-a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[0][0]*a[1][2]*a[2][1]
        return det



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
    print('-Введите 4 чтобы найти обратную матрицу (только 3x3)')
    choose = int(input())

    if choose == 1:
        transposed = transpose(rows, cols,matrix)
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
        multiplication(matrix,matrix2)
    elif choose == 4:
        tmin = transpose(3,3, (minor(matrix)))
        if determinant(matrix) == 0:
            raise ValueError("Определитель равен нулю!")


        det1 = 1/determinant(matrix)
        result = multiply(tmin,det1)
        print('Обратная матрица данной:')

        for row in result: print(row)





else:
    exit()





