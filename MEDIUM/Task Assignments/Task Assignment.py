def taskAssignment(k, tasks):
    optimalPairs = []
    sortedTasks = sorted(tasks) # Sort the given array tasks
    taskIndex = {}

    # store the indices of tasks
    for idx,value in enumerate(tasks):
        if value in taskIndex:
            taskIndex[value].append(idx)
        else:
            taskIndex[value]=[idx]
    i = 0
    while i<k:
        shortTask = sortedTasks[i] # Left most value
        longTask =  sortedTasks[len(sortedTasks)-1-i] # Right most value
        pair = [taskIndex[shortTask].pop(), taskIndex[longTask].pop()] # make the pair with shortest and longest tasks
        optimalPairs.append(pair)
        i+=1

    return optimalPairs