# Optimal Solution
def missingNumbers(nums):
    totalSum = sum(range(1, len(nums) + 3))  # Find all number's sum
    numSum = sum(nums)  # Find given number's sum
    sumDiff = totalSum - numSum  # Sum of missing numbers
    # Average of two numbers
    # One missing number will be smaller than the average
    # Another missing number will be greater than the average
    MissingSumAvg = sumDiff // 2
    firstHalfSum = 0
    secondHalfSum = 0
    for item in nums:
        if item <= MissingSumAvg:
            firstHalfSum += item
        else:
            secondHalfSum += item

    ExpectedFirstHalfSum = sum(range(1, MissingSumAvg + 1))
    ExpectedSecondHalfSum = sum(range(MissingSumAvg + 1, len(nums) + 3))

    return [ExpectedFirstHalfSum - firstHalfSum, ExpectedSecondHalfSum - secondHalfSum]

