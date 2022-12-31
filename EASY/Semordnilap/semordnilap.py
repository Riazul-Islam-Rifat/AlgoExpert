def semordnilap(words):
    # As the given list contains unique strings hence I am not using a separate set
    # If the strings are not unique then use set
    semordnilap_pair = []

    # Iterate the words list ->
    # reverse each word -> check the reverse whether it is in the given list or not

    for word in words:
        reversed = word[::-1]
        if reversed in words and reversed != word:  # Ignore palindrome
            semordnilap_pair.append([word, reversed])
            # To avoid multi occurance
            words.remove(word)
            words.remove(reversed)

    return semordnilap_pair