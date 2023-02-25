def mergeOverlappingIntervals(intervals):
    # Sort the input array based on the first (starting number) element of each intervals
    sorted_interval = sorted(intervals, key=lambda x: x[0])
    currentInterval = sorted_interval[0]
    mergedIntervals = [currentInterval]  # Initially taking the first element as an independent element

    for nextInterval in sorted_interval:

        if currentInterval[1] >= nextInterval[0]:
            currentInterval[1] = max(currentInterval[1], nextInterval[1])

        else:
            mergedIntervals.append(nextInterval)
            currentInterval = nextInterval

    return mergedIntervals



