def firstNonRepeatingCharacter(string):
    # Write your code here.
    tracker = {}
    for item in string:
        if item not in tracker:
            tracker[item]=1
        else:
            tracker[item]+=1

    for item in range(len(string)):
        if tracker[string[item]]==1:
            return item # Return the index of the string's first non-repeating character.
    return -1
