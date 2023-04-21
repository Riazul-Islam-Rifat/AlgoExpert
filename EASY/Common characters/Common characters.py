def commonCharacters(strings):
    # Find the smallest string from strings
    # All the characters of smallestString must be in other strings.
    smallestString = strings[0]
    for string in strings:
        if len(string) < len(smallestString):
            smallestString = string
    smallestString = set(smallestString)

    for string in strings:
        string = set(string)
        # Converting to list as we can't change size of set during iteration
        for char in list(smallestString):
            if char in string:
                continue
            else:
                smallestString.remove(char)
    return list(smallestString)