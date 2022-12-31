def isValidSubsequence(array, sequence):
    sequence_tracker = 0

    for item in array:

        if sequence_tracker == len(sequence):
            break

        if item == sequence[sequence_tracker]:
            sequence_tracker += 1

    return sequence_tracker == len(sequence)