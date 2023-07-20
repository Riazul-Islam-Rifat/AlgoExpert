def longestCommonSubsequence(str1, str2):
    # Number of rows = len(str2)+1
    # Number of columns = len(str1)+1
    # +1 because first row and column is empty string
    # Here the empty string is the base case
    lcs = [[[] for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    print(lcs)
    for i in range(1,len(str2)+1): # Row
        for j in range(1,len(str1)+1):# Col
            # -1 is used because we have empty string at first column and row
            if str2[i-1] == str1[j-1]: # If the last char is same of the two strings
                # We take the diagonal LCS and add the current char
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
            else:
                # We take the max lcs of the left and top position of the current position
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1],key=len)

    return lcs[-1][-1]