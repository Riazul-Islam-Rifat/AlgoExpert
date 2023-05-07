def validIPAddresses(string):
    IPaddress = []

    # For the first part [   . at 1st-3rd position]
    for i in range(1, min(len(string), 4)):
        currentIPaddress = ['', '', '', '']
        currentIPaddress[0] = string[:i]  # First part of the current address

        if not isValidPart(currentIPaddress[0]):
            continue  # If not a valid part then move the dot to the next position

        # If the first part is valid then look for the second part
        for j in range(i + 1, min(len(string), i + 4)):
            currentIPaddress[1] = string[i:j]  # Second part of the current address

            if not isValidPart(currentIPaddress[1]):
                continue  # If not a valid part then move the dot to the next position

            # If the second part is valid then look for the third part
            for k in range(j + 1, min(len(string), j + 4)):
                currentIPaddress[2] = string[j:k]  # Third part of the current address
                currentIPaddress[3] = string[k::]  # Fourth part of the current address

                if isValidPart(currentIPaddress[2]) and isValidPart(currentIPaddress[3]):
                    IPaddress.append('.'.join(currentIPaddress))
    return IPaddress


def isValidPart(IPpart):
    IntIP = int(IPpart)
    if IntIP > 255:
        return False
    return len(IPpart) == len(str(IntIP))  # Check for leading 0s.




