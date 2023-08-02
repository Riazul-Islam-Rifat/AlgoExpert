def maximumSumSubmatrix(matrix, size):
    # Take the sum of all indexes upto that index. Matrix size is desired index's row and col.
    sums = getSum(matrix)
    MaxSum = float('-inf')

    # We will start from the right-bottom corner of the given size's matrix
    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]

            TopBorderUsed = row - size < 0  # Provides True when touches top border
            if not TopBorderUsed:
                total -= sums[row - size][col]
            LeftBorderUsed = col - size < 0  # Provides True when touches left border
            if not LeftBorderUsed:
                total -= sums[row][col - size]

            TopOrLeftBorderUsed = TopBorderUsed or LeftBorderUsed
            if not TopOrLeftBorderUsed:
                # When no border is used we add
                total += sums[row - size][col - size]
                # As us was subtracted twice
            MaxSum = max(MaxSum, total)
    return MaxSum


def getSum(matrix):
    # Take another matrix to store the sum
    sums = [[0 for _ in range(len(row))] for row in matrix]

    # Set the sum of the top row and left column
    sums[0][0] = matrix[0][0]

    # Top row
    for i in range(1, len(matrix[0])):
        sums[0][i] = sums[0][i - 1] + matrix[0][i]

    # Left col
    for i in range(1, len(matrix)):
        sums[i][0] = sums[i - 1][0] + matrix[i][0]

    # Create the whole sums matrix
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = matrix[row][col] + sums[row][col - 1] + sums[row - 1][col] - sums[row - 1][col - 1]
            # Index value + Top index value + Left Index Value - Diagonal value [As it was addes 2 times]

    return sums



