def twoNumberSum(array, targetSum):
    tracker = []
    for item in array:
        # difference = targetSum-item
        # targetSum = difference + item
        # If difference in tracker then difference + item makes up the targetSum
        if targetSum-item not in tracker:
            tracker.append(item)
        else:
            return [targetSum-item, item]

    return []
