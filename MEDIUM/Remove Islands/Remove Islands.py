def removeIslands(matrix):
    # Remove islands those are not adjacent with border islands
    # Traverse only the border row and columns
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1

            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue

            TraverseBorderMakeAdjacentIslandsTwo(row, col, matrix)

    # Traverse the changed matrix and update value with desired value
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 2:
                matrix[row][col] = 1

            elif matrix[row][col] == 1:
                matrix[row][col] = 0
    return matrix


# Traverse matrix
def TraverseBorderMakeAdjacentIslandsTwo(row, col, matrix):
    dfs_stack = [[row, col]]
    while len(dfs_stack) > 0:
        current_item = dfs_stack.pop()
        current_row, current_col = current_item
        # if matrix[current_row][current_col]==0 or matrix[current_row][current_col]==2:
        #     continue
        matrix[current_row][current_col] = 2

        neighbors = getNeighbors(current_row, current_col, matrix)
        for item in neighbors:
            neighbor_row, neighbor_col = item
            # Without this check we might add some elements again and again.
            if matrix[neighbor_row][neighbor_col] != 1:
                continue
            dfs_stack.append(item)


# Get neighbors
def getNeighbors(row, col, matrix):
    neighbors = []
    # UP
    if row - 1 >= 0:
        neighbors.append([row - 1, col])
    # DOWN
    if row < len(matrix) - 1:
        neighbors.append([row + 1, col])

    # Right
    if col < len(matrix[row]) - 1:
        neighbors.append([row, col + 1])
    # Left
    if col > 0:
        neighbors.append([row, col - 1])

    return neighbors


















