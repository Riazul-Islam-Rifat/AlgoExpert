def largestIsland(matrix):
    # Brute force algorithm
    maxLand = 0
    # We will pick 1 and traverse 0s around this 1
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                continue
            LandSize = GetLandSize(row, col, matrix)  # Here we get a land size for a particular 1

            maxLand = max(maxLand, LandSize)
    return maxLand


def GetLandSize(row, col, matrix):
    # Keep tracks the visited nodes
    visited = [[False for _ in row] for row in matrix]
    size = 1  # Counting the 1 which will be converted to 0.

    nodesToExplore = GetNeighbors(row, col, matrix)  # Find the neighbor 0 nodes for that 1

    # DFS implementation
    while len(nodesToExplore):
        node = nodesToExplore.pop()  # We pick a node
        row, col = node[0], node[1]  # Find it's[node] position

        if visited[row][col] == True:  # If that node is visited then continue with other nodes
            continue

        visited[row][col] = True  # Otherwise make that node visited
        # We explored/visited a new node hence increase the size
        size += 1
        # Now find the neighbor nodes for that picked node and add these with nodesToExplore as we are traversing in depth
        neighbors = GetNeighbors(row, col, matrix)

        nodesToExplore += neighbors

    # After traversing all possible 0s for that particular 1 return the size
    return size


def GetNeighbors(row, col, matrix):
    neighbors = []
    # Up
    if row > 0 and matrix[row - 1][col] != 1:  # We will only pick the 0s
        neighbors.append([row - 1, col])
    # Bottom
    if row < len(matrix) - 1 and matrix[row + 1][col] != 1:
        neighbors.append([row + 1, col])
    # Left
    if col > 0 and matrix[row][col - 1] != 1:  # We will only pick the 0s
        neighbors.append([row, col - 1])
    # Right
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] != 1:
        neighbors.append([row, col + 1])
    return neighbors













