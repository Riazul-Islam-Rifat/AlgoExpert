
def phoneNumberMnemonics(phoneNumber):
    # A list to create each of the Mnemonics
    # Length of each Mnemonics will be same as the length of phoneNumber
    currentMnemonics = ["0"] * len(phoneNumber)
    # Store all the Mnemonics here
    Mnemonics = []
    # The recursive function
    MnemonicsHelper(0, phoneNumber, currentMnemonics, Mnemonics)  # Starting with 0 index
    return Mnemonics


def MnemonicsHelper(idx, phoneNumber, currentMnemonics, Mnemonics):  # Starting with 0 index
    # The base case
    if idx == len(phoneNumber):  # When index number exceeds the limit. [Done for all indexes]
        Mnemonic = ''.join(currentMnemonics)  # This takes O(n) time
        Mnemonics.append(Mnemonic)

    else:
        digit = phoneNumber[idx]  # Digit of the phone number
        letters = chars[digit]  # Characters associated with that digit
        for letter in letters:
            currentMnemonics[idx] = letter  # Update the index with the corrsponding letter
            MnemonicsHelper(idx + 1, phoneNumber, currentMnemonics, Mnemonics)  # Recursive call for the next indexes


# Characters associated with digits
chars = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]

}