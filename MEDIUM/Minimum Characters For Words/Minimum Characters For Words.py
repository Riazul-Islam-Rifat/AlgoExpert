def minimumCharactersForWords(words):
    # Frequency of character that is occurred most in a word
    maxFreq = {}
    for item in words:
        # Frequency of character in the current word
        currentWordFreq = CurrentWordFrequency(item)
        for key in currentWordFreq:
            if key in maxFreq:
                maxFreq[key] = max(currentWordFreq[key], maxFreq[key])
            else:
                maxFreq[key] = currentWordFreq[key]

    output = []
    for key in maxFreq:
        for i in range(maxFreq[key]):
            output.append(key)
    return output

def CurrentWordFrequency(word):
    freq = {}
    for item in word:
        if item not in freq:
            freq[item]=0
        freq[item]+=1

    return freq