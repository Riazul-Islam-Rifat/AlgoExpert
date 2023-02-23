def longestPeak(array):
    longestPeak = 0
    i = 1
    while i < len(array) - 1:
        currentPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
        if not currentPeak:
            i += 1
            continue

        peakLeft = i - 2
        peakRight = i + 2

        while peakLeft >= 0 and array[peakLeft] < array[peakLeft + 1]:
            peakLeft -= 1

        while peakRight < len(array) and array[peakRight] < array[
            peakRight - 1]:  # peakRight < len(array) as we find peak for peakRight
            peakRight += 1

        currentPeakLength = peakRight - peakLeft - 1
        longestPeak = max(longestPeak, currentPeakLength)
        i = peakRight

    return longestPeak
