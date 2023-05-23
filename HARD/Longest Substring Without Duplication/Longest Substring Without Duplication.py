
def longestSubstringWithoutDuplication(string):
    # Dictionary to track the characters and their index
    lastSeen = {}
    # In subString we store the indexes of the longest substring without duplication
    # Initially the first character is the longest one
    subString = [0,1]
    # startIdx to track the start index of the longest substring
    # Initially it's 0
    startIdx = 0

    for idx,char in enumerate(string):
        if char in lastSeen: # When we find a duplicate character, we update the startIdx so that the duplicate character is not included is our subString
            startIdx = max(startIdx,lastSeen[char]+1)

        if subString[1]-subString[0]< idx+1 - startIdx: # If the current subString is smaller then we update the subString
            subString = [startIdx,idx+1]
        # If we find the character for the first time then we add it to the dictionary else we update the index
        lastSeen[char] = idx

    # Return the subString
    return string[subString[0]:subString[1]]