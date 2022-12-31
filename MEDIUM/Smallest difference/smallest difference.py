def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    arrayOnePointer = 0
    arrayTwoPointer = 0
    smallest_diff = float('inf')
    smallestPair = []
    difference = 0

    while arrayOnePointer < len(arrayOne) and arrayTwoPointer < len(arrayTwo):

        num1 = arrayOne[arrayOnePointer]
        num2 = arrayTwo[arrayTwoPointer]

        if num1 < num2:
            difference = num2 - num1
            arrayOnePointer += 1

        elif num1 > num2:
            difference = num1 - num2
            arrayTwoPointer += 1

        else:
            return [num1, num2]

        if smallest_diff > difference:
            smallest_diff = difference
            smallestPair = [num1, num2]

    return smallestPair