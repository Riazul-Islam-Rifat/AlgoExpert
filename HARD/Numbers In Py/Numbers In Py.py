def numbersInPi(pi, numbers):
    # Store the numbers in a hashTable so that we can access them within O(1) time
    numTable = {num:True for num in numbers}
    minSpace = getMinSpace(pi,numTable,{},0)
    return -1 if minSpace==float('inf') else minSpace

def getMinSpace(pi,numTable,cache,idx):
    # Base case
    if idx == len(pi):
        return -1
    # To avoid the same computation for multiple times
    if idx in cache:
        return cache[idx]

    minSpace = float('inf')
    for i in range(idx,len(pi)):
        prefix = pi[idx:i+1]
        if prefix in numTable:
            minSpaceInSuffix = getMinSpace(pi,numTable,cache,i+1)
            minSpace = min(minSpace,minSpaceInSuffix+1)
    cache[idx] = minSpace
    return cache[idx]