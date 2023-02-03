def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort(reverse=True)
    if fastest:
        blueShirtSpeeds.sort()
    else:
        blueShirtSpeeds.sort(reverse=True)

    expectedSpeed = 0

    for item in range(len(redShirtSpeeds)):
        expectedSpeed += (max(redShirtSpeeds[item], blueShirtSpeeds[item]))

    return expectedSpeed