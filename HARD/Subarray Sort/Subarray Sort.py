def subarraySort(array):
    # To track the minimum and maximum number of the unsorted subarray
    minNum = float('inf')
    maxNum = float('-inf')

    for i in range(len(array)):

        if IsNotSorted(i, array):
            minNum = min(minNum, array[i])  # Minimum value of the unsorted subarray
            maxNum = max(maxNum, array[i])  # Maximum value of the unsorted subarray

    # When the array is sorted
    if minNum == float('inf'):
        return [-1, -1]

    # Otherwise find the correct position(sorted index) of the minNum and maxNum

    # Position of the minimum value
    minNumIdx = 0
    while minNum >= array[minNumIdx]:
        minNumIdx += 1
    # Position of the maximum value
    maxNumIdx = len(array) - 1
    while maxNum <= array[maxNumIdx]:
        maxNumIdx -= 1

    return [minNumIdx, maxNumIdx]


def IsNotSorted(i, arr):
    if i == 0:
        return arr[i] > arr[i + 1]

    if i == len(arr) - 1:
        return arr[i] < arr[i - 1]

    return arr[i] > arr[i + 1] or arr[i] < arr[i - 1]