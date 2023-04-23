def longestPalindromicSubstring(string):
    # Starting and ending index of longest palindromic substring
    # A single character is a palindrome.
    # If there is no longest palindrome then the first character is the resulting one
    currentLongest = [0,1]
    for i in range(1,len(string)):
        oddPalindrome = getPalindrome(string,i-1,i+1) # aba, for odd number string
        evenPalindrome = getPalindrome(string,i-1,i) # bb, for even number string
        # Find the longest one in between oddPalindrome and evenPalindrome
        longest = max(oddPalindrome,evenPalindrome, key = lambda x:x[1]-x[0])
        # Update the currentLongest palindrome
        currentLongest = max(longest,currentLongest, key = lambda x:x[1]-x[0])

    return string[currentLongest[0]:currentLongest[1]]

def getPalindrome(string,leftIdx,rightIdx):
    while leftIdx>= 0 and rightIdx<len(string):
        if string[leftIdx]!=string[rightIdx]:
            break
        leftIdx-=1
        rightIdx+=1

    return [leftIdx+1,rightIdx]