def get_matrix (n, m, value):             # Объявите функцию get_matrix и напишите в ней параметры n, m и value
    matrix = []                           # Создайте пустой список matrix внутри функции get_matrix
    for i in range(n):                    # Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов
        matrix.append([])                 # В первом цикле добавляйте пустой список в список matrix
        for j in range(m):                # Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            matrix[i].append(value)       # Во втором цикле пополняйте ранее добавленный пустой список значениями value
    print(matrix)                         # После всех циклов верните значение переменной matrix
get_matrix(4, 2, 13)         # Выведите на экран(консоль) результат работы функции get_matrix