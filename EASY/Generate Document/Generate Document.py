from collections import Counter


def generateDocument(characters, document):
    character_count = Counter(characters)

    for item in document:

        # This takes O(1) time as character_count Dictionary. Same as set
        if item not in character_count or character_count[item] == 0:
            return False

        character_count[item] -= 1

    return True