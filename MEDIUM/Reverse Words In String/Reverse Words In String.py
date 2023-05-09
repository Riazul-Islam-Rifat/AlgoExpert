def reverseWordsInString(string):
    # Find all the separate words, spaces and store in the words list
    words = []
    startOfWord = 0
    for i in range(len(string)):
        if string[i] == ' ':  # Then we have found a word
            # Append the word in the word list
            words.append(string[startOfWord:i])
            startOfWord = i  # Update the startOfWord once a word is created

        elif string[startOfWord] == ' ':  # When the current character is not space but the start is space
            words.append(' ')
            startOfWord = i

    # Append the last word
    words.append(string[startOfWord:len(string)])
    # Now reverse the words list
    start = 0
    end = len(words) - 1

    while start < end:
        words[start], words[end] = words[end], words[start]
        start += 1
        end -= 1
    # make a string with the reversed list and return
    return ''.join(words)



