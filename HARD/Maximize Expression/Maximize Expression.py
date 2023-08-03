def maximizeExpression(array):
    if len(array) < 4:
        return 0

    maxOfA = [array[0]]  # This array will store the max value of a
    maxOfAminusB = [float('-inf')] * 1  # This array will store max value a-b
    maxOfAminusBplusC = [float('-inf')] * 2  # This array will store max value a-b+c
    maxOfAminusBplusCminusD = [float('-inf')] * 3  # This array will store max value a-b+c-d

    for i in range(1, len(array)):
        curMax = max(maxOfA[i - 1], array[i])
        maxOfA.append(curMax)

    for i in range(1, len(array)):
        curMax = max(maxOfAminusB[i - 1], maxOfA[i - 1] - array[i])
        maxOfAminusB.append(curMax)

    for i in range(2, len(array)):
        curMax = max(maxOfAminusBplusC[i - 1], maxOfAminusB[i - 1] + array[i])
        maxOfAminusBplusC.append(curMax)

    for i in range(3, len(array)):
        curMax = max(maxOfAminusBplusCminusD[i - 1], maxOfAminusBplusC[i - 1] - array[i])
        maxOfAminusBplusCminusD.append(curMax)

    return maxOfAminusBplusCminusD[-1]


