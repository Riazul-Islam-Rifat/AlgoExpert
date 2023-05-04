def groupAnagrams(words):
    anagrams = {}

    for word in words:
        # sort the word
        SortedWord = ''.join(sorted(word))  # sorted(word) returns a list of characters, and then we join chars
        if SortedWord in anagrams:
            anagrams[SortedWord].append(word)
        else:
            anagrams[SortedWord] = [word]

    return list(anagrams.values())



