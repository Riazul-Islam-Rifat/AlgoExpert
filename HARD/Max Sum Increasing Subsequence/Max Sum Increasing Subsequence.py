def maxSumIncreasingSubsequence(array):
    # Dynamic programming
    sums = array[:]  # Copy the array as sum will be at least the value of an index
    sequences = [None] * len(array)  # Every index contains the previous index that is used in the sum sequence

    # Find the max strictly increasing sum upto the current index(inclusive).
    MaxSumIdx = 0  # Track the index where the max sum is found.

    for i in range(len(array)):
        currentNum = array[i]

        for j in range(0, i):
            prevNum = array[j]
            if prevNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j  # Store the previous index that is used in sum
        if sums[i] > sums[MaxSumIdx]:
            MaxSumIdx = i

    return [sums[MaxSumIdx], FindSequence(array, sequences, MaxSumIdx)]


def FindSequence(arr, sqncs, currIdx):
    sqnc = []

    while currIdx is not None:
        sqnc.append(arr[currIdx])
        currIdx = sqncs[currIdx]
    # We store the numbers in opposite order hence we reverse it
    return list(reversed(sqnc))
