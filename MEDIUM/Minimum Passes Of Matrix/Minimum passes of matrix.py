def minimumPassesOfMatrix(matrix):
    # Find the position of all positive number
    queue = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                queue.append([row, col])
    passes = ConvertToPositive(matrix, queue)
    if not ContainPositive(matrix):  # When it is impossible to convert all the negative numbers into positive form
        return -1
    else:
        return passes


def ConvertToPositive(matrix, queue):
    passes = -1
    while len(queue) > 0:
        numOfPositiveNumber = len(queue)

        while numOfPositiveNumber > 0:
            positiveNumberIndex = queue.pop(0)
            row, col = positiveNumberIndex
            neighbors = findNeighbors(matrix, row, col)
            for item in neighbors:
                r, c = item
                if matrix[r][c] < 0:
                    matrix[r][c] = matrix[r][c] * -1
                    queue.append([r, c])

            numOfPositiveNumber -= 1
        passes += 1

    return passes


def findNeighbors(matrix, row, col):
    neighbors = []

    # UP
    if row - 1 >= 0:
        neighbors.append([row - 1, col])
    # DOWN
    if row + 1 <= len(matrix) - 1:
        neighbors.append([row + 1, col])
    # RIGHT
    if col + 1 <= len(matrix[row]) - 1:
        neighbors.append([row, col + 1])
    # LEFT
    if col - 1 >= 0:
        neighbors.append([row, col - 1])

    return neighbors


def ContainPositive(matrix):
    flag = True
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < 0:
                flag = False
                return flag
    return flag




