def riverSizes(matrix):
    # Output array that contains river size
    size = []
    # Creating visited list to track whether an elemsnt of matrix in visited or not
    visited = [[False for item in row] for row in matrix]

    # Traverse the matrix

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col]:
                continue

            # If the node/element is not traversed yet then
            traverseNode(row, col, matrix, visited, size)
    return size


def traverseNode(row, col, matrix, visited, size):
    rivers = 0
    # Stack for DFS
    toTraverse = [[row, col]]
    while len(toTraverse):
        node = toTraverse.pop()
        row = node[0]
        col = node[1]

        if visited[row][col]:
            continue

        visited[row][col] = True  # make the node visited

        if matrix[row][col] == 0:
            continue

        rivers += 1
        neighborNodes = getNeighbors(row, col, matrix, visited)
        for item in neighborNodes:
            toTraverse.append(item)

    if rivers > 0:
        size.append(rivers)


def getNeighbors(row, col, matrix, visited):
    neighbors = []

    if row > 0 and not visited[row - 1][col]:
        neighbors.append([row - 1, col])

    if row < len(matrix) - 1 and not visited[row + 1][col]:
        neighbors.append([row + 1, col])

    if col > 0 and not visited[row][col - 1]:
        neighbors.append([row, col - 1])

    if col < len(matrix[0]) - 1 and not visited[row][col + 1]:
        neighbors.append([row, col + 1])

    return neighbors






