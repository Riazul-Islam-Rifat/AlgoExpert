def staircaseTraversal(height, maxSteps):
  NumberOfWays = 0
  waysToTop = [1]

  for currentHeight in range(1,height+1):
    startOfWindow = currentHeight - maxSteps -1
    endOfWindow = currentHeight -1

    if startOfWindow >= 0:
      NumberOfWays -= waysToTop[startOfWindow]

    NumberOfWays += waysToTop[endOfWindow]
    waysToTop.append(NumberOfWays)
    print(waysToTop)
  return NumberOfWays
