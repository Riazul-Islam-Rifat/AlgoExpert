def threeNumberSum(array, targetSum):
    triplets = []
    array.sort()

    for item in range(len(array) - 2):
        runningSum = array[item]
        leftPointer = item + 1
        rightPointer = len(array) - 1

        while leftPointer < rightPointer:
            currentSum = runningSum + array[leftPointer] + array[rightPointer]

            if currentSum == targetSum:
                triplets.append([array[item], array[leftPointer], array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1

            elif currentSum < targetSum:
                leftPointer += 1

            else:
                rightPointer -= 1
    return triplets
