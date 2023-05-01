# Optimal solution
def oneEdit(stringOne, stringTwo):
    lenOne, lenTwo = len(stringOne), len(stringTwo)
    # If length difference is greater than one then there is no way to make two strings equal within one edit
    if abs(lenOne - lenTwo) > 1:
        return False
    idxOne = 0
    idxTwo = 0
    edited = False
    while idxOne < lenOne and idxTwo < lenTwo:
        if stringOne[idxOne] != stringTwo[idxTwo]:
            # If previously edited return False as already edited once
            if edited:
                return False
            # If char doesn't match for the first time then make an edit
            edited = True
            if lenOne > lenTwo:
                idxOne += 1
            elif lenOne < lenTwo:
                idxTwo += 1
            else:
                idxOne += 1
                idxTwo += 1
        else:
            idxOne += 1
            idxTwo += 1
    return True






