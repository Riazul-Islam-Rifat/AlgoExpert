def zigzagTraverse(array):
    result = []
    row, col = 0, 0  # We are starting from top left
    goingDown = True  # We will start by going down first. [Mentioned in the question]
    height = len(array) - 1  # Number of rows
    width = len(array[0]) - 1  # Number of column. All row will have the same length
    while not outOfBound(row, col, height, width):
        # When we are not out of bound we add the element in our result list
        result.append(array[row][col])
        # When we are traversing to the downwards
        if goingDown:
            if col == 0 or row == height:
                # If we are at the left most side of the array or at the last row we can't go down furthermore
                # Hence we change our direction
                goingDown = False

                # If we are at the last row, we shift the column to the right instead of going down
                if row == height:
                    col += 1
                else:  # We go straight down, means we forward to the next row
                    row += 1
            else:
                row += 1
                col -= 1
        else:  # When we are going Up
            if col == width or row == 0:
                # If we are at the right most side of the array or at the top most row we can't go up furthermore
                # Hence we change our direction
                goingDown = True

                if col == width:  # Instead of going right we straight go down
                    row += 1
                else:  # We go right
                    col += 1
            else:
                col += 1
                row -= 1
    return result


def outOfBound(row, col, height, width):
    return row > height or row < 0 or col > width or col < 0
