# Я копирую полученную функцией матрицу, чтобы, опираясь на данные из полученной матрицы, заполнить скопированную.
# Иду по элементам скопированной матрицы, исключая первый столбец и первую строку, чтобы заполнить ее

def countSquares(matrix) -> int:
    
    dp_table = [row for row in matrix]  # Копирую

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            
            if matrix[i][j]:   # Если в изначальной матрице элемент с такими же индексами не = 0, то                
               dp_table[i][j] = 1 + min(dp_table[i][j-1], dp_table[i-1][j-1], dp_table[i-1][j])
    
    return sum([sum(i) for i in dp_table])

# Сложность алгоритма О (n ** 2)