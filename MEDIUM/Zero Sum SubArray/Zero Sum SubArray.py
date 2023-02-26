def zeroSumSubarray(nums):
    subArraySum = set([0])
    currentSum = 0

    for item in nums:
        currentSum+=item
        if currentSum in subArraySum:
            return True

        subArraySum.add(currentSum)

    return False
