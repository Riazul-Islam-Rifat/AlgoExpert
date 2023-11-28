def transposeMatrix(matrix):
    TM = [[None for i in range(len(matrix))] for _ in range(len(matrix[0]))]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            TM[col][row] = matrix[row][col]

    return TM  # Transpose Matrix