def maxSubsetSumNoAdjacent(array):
    if len(array)==0:
        return 0

    if len(array)==1:
        return array[0]

    first = array[0] # Left
    second = max(array[0],array[1]) # Right (Always has the max)

    # First might be equal to the second

    for item in range(2,len(array)):
        currentSum = max(first+array[item],second) # Current sum will hold the max
        first = second # First (left) becomes the previous max
        second = currentSum # second (Right) becomes the max

    return second