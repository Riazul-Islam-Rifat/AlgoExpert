def minimumWaitingTime(queries):
    # If we sort the array waiting time will be minimal. Ex-> [6,1] waiting time - 6 but for [1,6] waiting time - 1
    queries.sort()
    waitingTime = 0

    for index, duration in enumerate(queries):
        waitingTime += (len(queries) - (index + 1)) * duration

    return waitingTime

