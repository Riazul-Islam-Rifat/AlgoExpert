# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Time complexity:
        # O(n^2)
        # Space complexity
        # O(n^2)
        # Construct suffix trie

        for i in range(len(string)):
            root = self.root
            for j in range(i, len(string)):
                letter = string[j]  # Letter that I want to insert
                if letter not in root:
                    root[letter] = {}  # Create kinda another root
                root = root[letter]  # Update the root
            # Add * at the end
            root[self.endSymbol] = True

    # Time complexity:
    # O(n)
    # Space complexity
    # O(1)
    def contains(self, string):
        root = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in root:
                return False
            root = root[letter]  # Move to the next
        # Add * at the end
        return self.endSymbol in root  # This will be true when the whole string will be found
