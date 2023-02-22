def spiralTraverse(array):
    output = []
    sRow = 0
    sCol = 0
    eRow = len(array) - 1
    eCol = len(array[0]) - 1

    while sRow <= eRow and sCol <= eCol:
        # Left to right
        for col in range(sCol, eCol + 1):
            output.append(array[sRow][col])

        # Top to bottom
        for row in range(sRow + 1, eRow + 1):
            output.append(array[row][eCol])

        # Right to left
        for col in range(eCol - 1, sCol - 1, -1):
            # To handle when there is single row [Single row will be printed in first for loop]
            if sRow == eRow:
                break
            output.append(array[eRow][col])

        # Bottom to top
        for row in range(eRow - 1, sRow, -1):
            # To handle when there is a single column [Single column will be printed in second for loop]
            if sCol == eCol:
                break
            output.append(array[row][sCol])

        sRow += 1
        sCol += 1
        eRow -= 1
        eCol -= 1

    return output




