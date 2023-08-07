def diceThrows(numDice, numSides, target):
    # Create a 2D array and update it gradually to find the result
    # Row is num of dice and col is num of target
    numOfWays = [[0 for i in range(target+1)] for _ in range(numDice+1)]
    # When there is no dice with no target then 1 way to reach, just do nothing
    numOfWays[0][0]=1
    # When number of dice greater than target there is no way to reach it
    # When there is no dice but still we have target there is no way to reach

    for currentNumDice in range(1,numDice+1):
        for currentTarget in range(0,target+1):
            numOfWaysToReachTarget = 0
            for currentNumSides in range(1,min(currentTarget,numSides)+1):
                # Add the numOfWays from 1 to upto that target to get the value for [currentNumDice][currentTarget] . Here range can never exceed numSides
                numOfWaysToReachTarget+= numOfWays[currentNumDice-1][currentTarget-currentNumSides]
            numOfWays[currentNumDice][currentTarget] = numOfWaysToReachTarget

    return numOfWays[numDice][target]
