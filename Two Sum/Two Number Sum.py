def twoNumberSum(array, targetSum):

    # As the given array contains distinct integers only hence I am not using any separate set for my solution
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
