def countSquares(points):
    # Create a set to check the coordinate's existence is the given list within o(1) time
    pointSet = set()
    for item in points:
        # We can't add list in a set as list is mutable. Hence list is not hashable
        pointSet.add(pointString(item))
    squareCounter = 0
    for pointA in points:
        for pointB in points:
            if pointA == pointB:
                continue
            # Take two co-ordinates (x1y1, x2y2). Assume two points are diagonally connected in the square.
            # We will find the rest two diagonally connected points. If these two points exist in the given points list:
            # then all the four points together create a square

            # Step 1: Find the mid point of the pointA and pointB
            midCoordinate = [(pointA[0] + pointB[0]) / 2, (pointA[1] + pointB[1]) / 2]
            # Step 2: Find xDistance and yDistance from mid.
            xAxisDistance = pointB[0] - midCoordinate[0]
            yAxisDistance = pointB[1] - midCoordinate[1]

            # OR
            # xAxisDistance = pointA[0] - midCoordinate[0]
            # yAxisDistance = pointA[1] - midCoordinate[1]

            # Step:3 find the diagonal points
            pointC = [midCoordinate[0] + yAxisDistance, midCoordinate[1] - xAxisDistance]
            pointD = [midCoordinate[0] - yAxisDistance, midCoordinate[1] + xAxisDistance]

            if pointString(pointC) in pointSet and pointString(pointD) in pointSet:
                squareCounter += 1

    return squareCounter / 4  # We will count a single square 4 times, hence divide by 4 to get the actual answer


def pointString(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(point[0]), int(point[1])]
    return ''.join(str(val) for val in point)
    # return ''.join([str(val) for val in point]) --> This also works