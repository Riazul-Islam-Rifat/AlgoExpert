def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    if blueShirtHeights[0] == redShirtHeights[0]:
        return False

    Tallest_Student_Shirt = 'BLUE' if blueShirtHeights[0] > redShirtHeights[0] else 'RED'

    for item in range(len(redShirtHeights)):
        if Tallest_Student_Shirt == "BLUE":
            if blueShirtHeights[item] <= redShirtHeights[item]:
                return False

        else:
            if blueShirtHeights[item] >= redShirtHeights[item]:
                return False

    return True