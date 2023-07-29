def knapsackProblem(items, capacity):
    # Create a 2D array. Columns == capacity ; Row = Number of items in items list
    knapsack = [[0 for item in range(capacity + 1)] for y in range(len(items) + 1)]

    for row in range(1, len(items) + 1):  # Index 0 is the base case
        value = items[row - 1][0]  # Value of the item
        weight = items[row - 1][1]  # Weight of the item
        # For each row/item we check upto the given capacity. [0-capacity]
        for col in range(capacity + 1):
            if weight > col:  # When weight greater than capacity
                # We take the max upto this capacity, which is it's previous row's value
                knapsack[row][col] = knapsack[row - 1][col]
            else:  # When capacity is greater than the weight
                knapsack[row][col] = max(knapsack[row - 1][col], knapsack[row - 1][col - weight] + value)
                # Here knapsack[row-1][col-weight]+value provides the max value which never exceeds capacity

    return [knapsack[-1][-1], usedItems(knapsack, items)]


# Backtracking
def usedItems(knapsack, items):
    sequence = []
    # Provides the last index
    item = len(knapsack) - 1  # Row
    capacity = len(knapsack[0]) - 1  # Column

    while item > 0:
        if knapsack[item][capacity] == knapsack[item - 1][capacity]:  # Means current item is not used
            item -= 1
        else:
            sequence.append(item - 1)  # -1 as the first [0th] index is the base case
            capacity -= items[item - 1][1]  # Capacity =  capacity - current item's capacity
            item -= 1

        if capacity == 0:  # Then we have reached to the base case
            break
    return list(reversed(sequence))

