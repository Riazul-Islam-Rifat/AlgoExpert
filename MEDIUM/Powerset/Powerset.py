

def powerset(array):
    subset = [[]]
    for item in array:
        # We can't use for i in subset, because it may create an infinite loop
        for i in range(len(subset)):
            subset.append(subset[i] + [item])

    return subset

